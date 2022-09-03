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
- **.gitignore** Git ignore file
- **app/templates/** HTML templates used by flask for the web app
- **app/run.py**  Needed to start flask app
- **data/disaster_categories.csv** File containing categories data
- **data/disaster_messages.csv** File containing messages
- **data/Disaster.db** Database with processed data
- **data/process_data.py** Python script used for ETL
- **models/train_classifier.py** Python script used to train the model

# Results
1. RandomForest
   - Best score 

       | total | precision | recall |  f1-score | support |
       |----------|----------|:-------------:|------:|------:|
       | 0 | 0.95 | 0.99 | 0.97 | 172321 |
       | 1 | 0.82 | 0.49 | 0.61 | 16423 |
       | 2 | 0.60 | 0.30 | 0.40 | 16423 |
       | accuracy |   |   |  0.95 | 188784 |
       | macro avg | 0.79 | 0.59 | 0.66 | 188784 |
       | wighed avg | 0.94 |0.95 | 0.94 | 188784 |

   - Best params
        
            {'clf__min_samples_split': 2, 'clf__n_estimators': 100, 'vect__ngram_range': (1, 2)} 

    <details>
    <summary>📚 Click to see all scores</summary>

    | related | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 35 |
    | 1 | 0.50 | 1.00 | 0.67 | 1 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.75 | 0.99 | 0.83 | 36 |
    | wighed avg | 0.99 |0.97 | 0.98 | 36 |

    | request | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 |1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | offer | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.91 | 1.00 | 0.95 | 30 |
    | 1 | 1.00 | 0.50 | 0.67 | 6 |
    | accuracy |   |   |  0.92 | 36 |
    | macro avg | 0.95 | 0.75 | 0.81 | 36 |
    | wighed avg | 0.92 |0.92 | 0.90 | 36 |

    | aid_related | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 | 0.49 | 36 |
    | wighed avg | 1.00 |0.97 | 0.99 | 36 |

    | medical_help | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 | 0.49 | 36 |
    | wighed avg | 1.00 |0.97 | 0.99 | 36 |

    | medical_products | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 32 |
    | 1 | 1.00 | 0.50 | 0.67 | 4 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.75 | 0.82 | 36 |
    | wighed avg | 0.95 |0.94 | 0.94 | 36 |

    | search_and_rescue | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 36 |
    | accuracy |   |   | 1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | security | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 32 |
    | 1 | 1.00 | 0.50 | 0.67 | 4 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.75 | 0.82 | 36 |
    | wighed avg | 0.95 |0.94 | 0.94 | 36 |

    | military | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.91 | 1.00 | 0.95 | 30 |
    | 1 | 1.00 | 0.50 | 0.67 | 6 |
    | accuracy |   |   |  0.92 | 36 |
    | macro avg | 0.95 | 0.75 | 0.81 | 36 |
    | wighed avg | 0.92 |0.92 | 0.90 | 36 |

    | child_alone | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 | 0.49 | 36 |
    | wighed avg | 1.00 |0.97 | 0.99 | 36 |

    | water | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 36 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 |1.00 | 1.00 | 36 |

    | food | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.97 | 1.00 | 0.98 | 32 |
    | 1 | 1.00 | 0.75 | 0.86 | 4 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.98 | 0.88 | 0.92 | 36 |
    | wighed avg | 0.97 |0.97 | 0.97 | 36 |

    | shelter | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 33 |
    | 1 | 1.00 | 0.33 | 0.50 | 3 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.67 | 0.74 | 36 |
    | wighed avg | 0.95 |0.94 | 0.93 | 36 |

    | clothing | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 |1.00 | 1.00 | 36 |

    | money | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.85 | 1.00 | 0.92 | 29 |
    | 1 | 1.00 | 0.29 | 0.44 | 7 |
    | accuracy |   |   |  0.86 | 36 |
    | macro avg | 0.93 | 0.64 | 0.68 | 36 |
    | wighed avg | 0.88 |0.86 | 0.83 | 36 |

    | missing_people | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 32 |
    | 1 | 1.00 | 0.50 | 0.67 | 4 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.75 | 0.82 | 36 |
    | wighed avg | 0.95 |0.94 | 0.94 | 36 |

    | refugees | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 33 |
    | 1 | 1.00 | 0.33 | 0.50 | 3 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.67 | 0.74 | 36 |
    | wighed avg | 0.95 |0.94 | 0.93 | 36 |

    | death | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 32 |
    | 1 | 1.00 | 1.00 | 1.00 | 4 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 |1.00 | 1.00 | 36 |

    | other_aid | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 | 0.49 | 36 |
    | wighed avg | 1.00 |0.97 | 0.99 | 36 |

    | infrastructure_related | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 32 |
    | 1 | 1.00 | 0.50 | 0.67 | 4 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.75 | 0.82 | 36 |
    | wighed avg | 0.95 |0.94 | 0.94 | 36 |

    | transport | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 32 |
    | 1 | 1.00 | 0.50 | 0.67 | 4 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.75 | 0.82 | 36 |
    | wighed avg | 0.95 |0.94 | 0.94 | 36 |

    | buildings | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.0 | 1 |
    | accuracy |   |   | 1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 |1.00 | 1.00 | 36 |

    | electricity | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.97 | 1.00 | 0.99 | 34 |
    | 1 | 1.00 | 0.50 | 0.67 | 2 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.99 | 0.75 | 0.83 | 36 |
    | wighed avg | 0.97 |0.97 | 0.97 | 36 |

    | tools | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | hospitals | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | shops | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 | 1.00 | 36 |
    | wighed avg | 1.00 |1.00 | 1.00 | 36 |

    | aid_centers | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 36 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 |  1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | other_infrastructure | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.80 | 1.00 | 0.89 | 28 |
    | 1 | 1.00 | 0.12 | 0.22 | 8 |
    | accuracy |   |   |  0.81 | 36 |
    | macro avg | 0.90 | 0.56 |  0.56 | 36 |
    | wighed avg | 0.84 | 0.81 | 0.74 | 36 |

    | weather_related | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 |  0.49 | 36 |
    | wighed avg | 1.00 | 0.97 | 0.99 | 36 |

    | floods | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 |  1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | storm | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 33 |
    | 1 | 1.00 | 0.33 | 0.50 | 3 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.67 |  0.74 | 36 |
    | wighed avg | 0.95 | 0.94 | 0.93 | 36 |

    | fire | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.94 | 1.00 | 0.97 | 33 |
    | 1 | 1.00 | 0.33 | 0.50 | 3 |
    | accuracy |   |   |  0.94 | 36 |
    | macro avg | 0.97 | 0.67 |  0.74 | 36 |
    | wighed avg | 0.95 | 0.94 | 0.93 | 36 |

    | earthquake | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.56 | 1.00 | 0.72 | 18 |
    | 1 | 1.00 | 0.22 | 0.36 | 18 |
    | accuracy |   |   |  0.61 | 36 |
    | macro avg | 0.78 | 0.61 |  0.54 | 36 |
    | wighed avg | 0.78 | 0.61 | 0.54 | 36 |

    | cold | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 1.00 | 1.00 | 35 |
    | 1 | 1.00 | 1.00 | 1.00 | 1 |
    | accuracy |   |   |  1.00 | 36 |
    | macro avg | 1.00 | 1.00 |  1.00 | 36 |
    | wighed avg | 1.00 | 1.00 | 1.00 | 36 |

    | other_weather | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 0.88 | 1.00 | 0.94 | 29 |
    | 1 | 1.00 | 0.43 | 0.60 | 7 |
    | accuracy |   |   |  0.89 | 36 |
    | macro avg | 0.94 | 0.71 |  0.77 | 36 |
    | wighed avg | 0.90 | 0.89 | 0.87 | 36 |

    | direct_report | precision | recall |  f1-score | support |
    |----------|----------|:-------------:|------:|------:|
    | 0 | 1.00 | 0.97 | 0.99 | 36 |
    | 1 | 0.00 | 0.00 | 0.00 | 0 |
    | accuracy |   |   |  0.97 | 36 |
    | macro avg | 0.50 | 0.49 |  0.49 | 36 |
    | wighed avg | 1.00 | 0.97 | 0.99 | 36 |
    
    </details>
2. Many message types have very low samples (or none). We could consider removing them or aggregating them with other features.
3. We can consider to implement a vectorization of the complete text, and match it to the closest vec of the features to improve performance.
# License
You can use this in any way you want.