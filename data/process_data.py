import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath: str, categories_filepath: str) -> pd.DataFrame:
    '''loads data and return a pandas DataFrame
    
    input:
        messages_filepath (str): path to messages file
        categories_filepath (str): path to categories file

    output:
        df (pandas.DataFrame): dataframe containing messages and categories
    '''

    # load messages and categories to separate dataframes
    messages_df = pd.read_csv(messages_filepath)
    categories_df = pd.read_csv(categories_filepath)
    df = pd.merge(messages_df, categories_df, how='inner', on = 'id')

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    '''transforms the data in a way that can be processed by a ML classifier

    input:
        df (pandas.DataFrame): dataframe with messages and categories

    output:
        df (pandas.DataFrame): dataframe that can be processed by a ML classifier
    '''
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0, :]

    # extract the column names by removing the last 2 chars
    category_colnames = [cat[0:-2] for cat in row]
    # rename the columns
    categories.columns = category_colnames

    # extract the values and convert to int
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.split('-').str[1]
        
        # convert column from string to numeric
        categories[column] = categories[column].astype('int32')

    # drop the categories column for dataframe and concatenate new categories df
    df = pd.concat([df.drop('categories', axis=1), categories], axis=1)

    # remove duplicates
    df = df[~df.duplicated()]

    return df


def save_data(df: pd.DataFrame, database_filename: str) -> None:
    '''save data to sqlite db
    
    input:
        df (pandas.DataFrame): dataframe to save
        database_filename (str): path to sqlite db
    '''
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisasterMessages', engine, index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()