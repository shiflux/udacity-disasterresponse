# Udacity capstone project - Disaster Response Pipeline Project

# Table of Contents
1. [Installation](README.md#installation)
2. [Instructions](README.md#instructions)
3. [File Description](README.md#file-description)
4. [Results](README.md#results)
5. [Licensing, Authors and Acknowledgements](README.md#licensing-authors-and-acknowledgements)


# Installation
- Clone the repository
- Do one of the following
- 1.1 Install pipenv env
```
pipenv install
```
- 1.2 Install python modules with pip
```
pip install -r requirements.txt
```

# Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

# File Description
**.gitignore** Git ignore file
**app/templates/** HTML templates used by flask for the web app
**app/run.py**  Needed to start flask app
**data/disaster_categories.csv** File containing categories data
**data/disaster_messages.csv** File containing messages
**data/Disaster.db** Database with processed data
**data/process_data.py** Python script used for ETL
**models/train_classifier.py** Python script used to train the model

# Results
I tried to use both RandomForest and SVM for the classification.
1. RandomForest
   - Best score 

       |  | precision | recall |  f1-score | support |
       |----------|----------|:-------------:|------:|------:|
       | accuracy |   |   |  0.95 | 188784 |
       | macro avg | 0.89 | 0.56 | 0.64 | 188784 |
       | wighed avg | 0.94 |0.95 | 0.94 | 188784 |

   - Best params
        
            {'clf__min_samples_split': 2, 'clf__n_estimators': 200, 'vect__ngram_range': (1, 2)} 

2. SVM TODO
   - Best score 

       |  | precision | recall |  f1-score | support |
       |----------|----------|:-------------:|------:|------:|
       | accuracy |   |   |    |   |
       | macro avg |   |   |   |   |
       | wighed avg |   |   |   |   |

   - Best params
        
            {TODO} 

# License
You can use this in any way you want.