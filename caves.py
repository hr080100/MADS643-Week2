"""
This is the caves file that gets the caves data, 
cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

def read_caves(file_path):
    caves_raw = pd.read_csv(file_path)
    return caves_raw

def clean_caves(caves_data):
    caves_data = caves_data.loc[:, ['Cave_Name', 'County', 'Length_Mi', 'Lenght_Me',
                          'Depth_Ft', 'Depth_Me', 'State']]
    caves_data.rename(columns={'Lenght_Me':'Length_Me'}, inplace=True)
    return caves_data

def caves(file_path = 'data_files/caves_output.csv'):
    caves_raw = read_caves(file_path)
    caves_final = clean_caves(caves_raw)
    return caves_final
