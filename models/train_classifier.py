import sys

import pandas as pd

import numpy as np

import re

from sqlalchemy import create_engine

import pickle

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

def load_data(database_filepath: str) -> tuple[pd.Series, pd.DataFrame, list]:
    '''load data from sqlite db, table "DisasterMessages"
    
    input:
        database_filepath (str): path to sqlite db
        
    output:
        X (pd.Series)
        Y (pd.DataFrame)
        category_names (list)
    '''
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('DisasterMessages', engine)
    X = df['message']
    Y = df.drop(['id', 'message', 'original', 'genre'], axis=1)
    
    return X, Y, list(Y.columns)


def tokenize(text: str) -> list:
    '''Tokenizes a string of text

    input:
        text (str): input text

    output:
        List of tokens
    '''
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    # best random forest {'clf__estimator__min_samples_split': 4, 'clf__estimator__n_estimators': 200, 'vect__ngram_range': (1, 2)}
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(SVC()))
    ])
    
    # parameters = {
    #     'vect__ngram_range': ((1, 1), (1, 2)),
    #     'clf__estimator__n_estimators': [10, 50, 100, 200],
    #     'clf__estimator__min_samples_split': [2, 3, 4]
    # }
    parameters = {'clf__estimator__C': [0.1, 1, 10, 100, 1000], 
              'clf__estimator__gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'clf__estimator__kernel': ['rbf']} 
    return GridSearchCV(pipeline, parameters, n_jobs=3, verbose = 3)
    #return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    
    #for index in range(0, len(category_names)):
    #    print(category_names[index], classification_report(Y_test.values[index,:], y_pred[index,:]))
    
    print('total', classification_report(np.hstack(Y_test.values), np.hstack(y_pred)))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        nltk.download('stopwords')

        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        print(model.best_params_)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()