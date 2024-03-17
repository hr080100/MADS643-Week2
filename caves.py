"""
This is the caves file that gets the caves data, 
cleans the dataframe and return the refined dataframe
for further data analysis.
"""

# Importing the required libraries.
import pandas as pd

# Creating a function to read the caves csv file.
def read_caves(file_path):
    """
    This function reads the caves csv file
    and return it as a dataframe in its raw form.
    """
    caves_raw = pd.read_csv(file_path)
    return caves_raw

# Cleaning the caves dataframe.
def clean_caves(caves_data):
    """
    This function takes the caves dataframe
    and cleans it so that it can be used for further
    processing.
    """
    # Keeping the columns that are necessary.
    caves_data = caves_data.loc[:, ['Cave_Name', 'County', 'Length_Mi', 'Lenght_Me',
                          'Depth_Ft', 'Depth_Me', 'State']]
    # Renaming the columns correctly.
    caves_data.rename(columns={'Lenght_Me':'Length_Me'}, inplace=True)
    return caves_data

# Calling the created functions to get the final dataframe.
def caves(file_path = 'data_files/caves_output.csv'):
    """
    This function calls both the earlier functions and
    returns the final processed dataframe.
    """
    caves_raw = read_caves(file_path)
    caves_final = clean_caves(caves_raw)
    return caves_final
