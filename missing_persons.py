"""
This is the missing persons file that gets the missing persons
data, cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

def read_missing_persons(file_path):
    missing_persons_raw = pd.read_csv(file_path)
    return missing_persons_raw

def clean_missing_persons(missing_persons_data):
    missing_persons_data = missing_persons_data[['2', '4', '6', '8', '10', '12', '14',
                                       '16', '18', '20', '22']]
    missing_persons_data.columns = ['Case', 'DLC', 'Last_Name', 'First_Name', 'Age',
                               'City', 'County', 'State_Ab', 'Gender', 'Ethnicity', 'Date_Modified']

    age = []
    for i in missing_persons_data['Age']:
        if i.split(" ")[0] == '<':
            age.append(0)
        else:
            age.append(int(i.split(" ")[0]))
    missing_persons_data.loc[:,'Age'] = age
    us_states = pd.read_csv('data_files/us_states.csv')
    us_states = dict(us_states.values)

    missing_persons_data.loc[:, 'State'] = missing_persons_data.loc[:, 'State_Ab'].map(us_states)
    missing_persons_data.drop(columns = ['State_Ab'], inplace = True)
    missing_persons_data['DLC'] = pd.to_datetime(missing_persons_data['DLC'])

    return missing_persons_data

def missing_persons(file_path = 'data_files/missing_person_output.csv'):
    missing_persons_raw = read_missing_persons(file_path)
    missing_persons_final = clean_missing_persons(missing_persons_raw)
    return missing_persons_final
