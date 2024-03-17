"""
This is the county population file that gets the population
data, cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

# Creating a function to read the county population excel file.
def read_county_pop(file_path = 'data_files/county_pop.xlsx'):
    """
    This function reads the county population excel
    file and return it as a dataframe in its raw form.
    """
    county_pop_raw = pd.read_excel(file_path)
    return county_pop_raw

# Cleaning the county population dataframe.
def clean_county_pop(county_pop_data):
    """
    This function takes the county population dataframe
    and cleans it so that it can be used for further
    processing.
    """
    # Creating county and state lists to store the values separately.
    county = []
    state = []
    # Getting the county and state names form the county column.
    for i in county_pop_data.loc[:, 'County']:
        state.append(i.split(', ')[1])
        county.append((i.split(', ')[0])[1:])

    # Removing the parts of the county names not needed.
    names_delete = ['County', 'Borough', 'Area', 'Census', 'Municipality', 'Region', 'Planning']
    for i in enumerate(county):
        if county[i[0]].split()[-1] in names_delete:
            county[i[0]] = " ".join(county[i[0]].split()[:-1])
    for i in enumerate(county):
        if county[i[0]].split()[-1] in names_delete:
            county[i[0]] = " ".join(county[i[0]].split()[:-1])
    for i in enumerate(county):
        if county[i[0]].split()[-1] in names_delete:
            county[i[0]] = " ".join(county[i[0]].split()[:-1])

    # Adding the colunms of county and state names in the original database.
    county_pop_data['County'] = county
    county_pop_data['State'] = state

    return county_pop_data

# Calling the created functions to get the final dataframe.
def county_pop(file_path = 'data_files/county_pop.xlsx'):
    """
    This function calls both the earlier functions and
    returns the final processed dataframe.
    """
    county_pop_raw = read_county_pop(file_path)
    county_pop_final = clean_county_pop(county_pop_raw)
    return county_pop_final
