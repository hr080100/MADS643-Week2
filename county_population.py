"""
This is the county population file that gets the population
data, cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

def read_county_pop(file_path = 'data_files/county_pop.xlsx'):
    county_pop_raw = pd.read_excel(file_path)
    return county_pop_raw

def clean_county_pop(county_pop_data):
    county = []
    state = []
    for i in county_pop_data.loc[:, 'County']:
        state.append(i.split(', ')[1])
        county.append((i.split(', ')[0])[1:])

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

    county_pop_data['County'] = county
    county_pop_data['State'] = state

    return county_pop_data

def county_pop(file_path = 'data_files/county_pop.xlsx'):
    county_pop_raw = read_county_pop(file_path)
    county_pop_final = clean_county_pop(county_pop_raw)
    return county_pop_final
