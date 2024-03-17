"""
This is the missing persons file that gets the missing persons
data, cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

# Creating a function to read the missing persons csv file.
def read_missing_persons(file_path):
    """
    This function reads the missing persons csv file
    and return it as a dataframe in its raw form.
    """
    missing_persons_raw = pd.read_csv(file_path)
    return missing_persons_raw

# Cleaning the missing persons dataframe.
def clean_missing_persons(missing_persons_data):
    """
    This function takes the missing persons dataframe
    and cleans it so that it can be used for further
    processing.
    """
    # All the columns are twice, so keeping the one iteration.
    missing_persons_data = missing_persons_data.loc[:, ['2', '4', '6', '8', '10', '12', '14',
                                       '16', '18', '20', '22']]
    # Renaming the columns correctly.
    missing_persons_data.columns = ['Case', 'DLC', 'Last_Name', 'First_Name', 'Age',
                               'City', 'County', 'State_Ab', 'Gender', 'Ethnicity', 'Date_Modified']

    # Getting the age of the people in the desired form.
    age = []
    for i in missing_persons_data['Age']:
        if i.split(" ")[0] == '<':
            age.append(0)
        else:
            age.append(int(i.split(" ")[0]))
    missing_persons_data.loc[:,'Age'] = age

    # Getting the csv file that contains US state abbreviations
    # and full forms.
    us_states = pd.read_csv('data_files/us_states.csv')
    us_states = dict(us_states.values)

    # Creating a new column with the state full forms.
    missing_persons_data.loc[:, 'State'] = missing_persons_data.loc[:, 'State_Ab'].map(us_states)
    missing_persons_data.drop(columns = ['State_Ab'], inplace = True)

    # Changing the date of last contact of people to datetime format.
    missing_persons_data['DLC'] = pd.to_datetime(missing_persons_data['DLC'])

    return missing_persons_data

# Calling the created functions to get the final dataframe.
def missing_persons(file_path = 'data_files/missing_person_output.csv'):
    """
    This function calls both the earlier functions and
    returns the final processed dataframe.
    """
    missing_persons_raw = read_missing_persons(file_path)
    missing_persons_final = clean_missing_persons(missing_persons_raw)
    return missing_persons_final
