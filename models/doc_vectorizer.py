from sklearn.base import BaseEstimator, TransformerMixin
import spacy
import numpy as np
import pandas as pd
from sqlalchemy import except_all

SPACY_NLP = spacy.load('en_core_web_lg')

class MeanVectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, tokenizer):
        self.tokenizer=tokenizer

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        #print(pd.DataFrame(pd.Series(X).apply(self.vectorize).tolist()))
        return pd.DataFrame(pd.Series(X).apply(self.vectorize).tolist())

    def vectorize(self, x):
        tokens = self.tokenizer(x)

        vectors = np.asarray([
            lexeme.vector for token in tokens if (lexeme := SPACY_NLP.vocab[token]).has_vector
        ])

        if len(vectors) > 0:
            return vectors.mean(axis=0)
        else:
            width = SPACY_NLP.meta['vectors']['width']
            return np.zeros(width)