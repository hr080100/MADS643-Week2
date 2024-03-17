"""
This file takes in the missing persons, caves and county
population data and returns a grouped dataframe.
"""

# Importing the required libraries.
import pandas as pd
import numpy as np

def data_per_county(missing_persons, caves, county_pop):
    # Aggregate Caves Data: Count the number of caves by county
    caves_per_county = caves.groupby(['County', 'State']).size().reset_index(name='Cave_Count')

    # Aggregate Missing Persons Data: Count missing persons by county
    missing_per_county = missing_persons.groupby(['County',
                                                  'State']).size().reset_index(name='Missing_Count')

    # Merging caves data
    analysis_df = pd.merge(county_pop, caves_per_county,
                           on=['County', 'State'], how='left').fillna(0)

    # Merging missing persons data
    analysis_df = pd.merge(analysis_df, missing_per_county,
                           on=['County', 'State'], how='left').fillna(0)

    # Normalize the number of missing persons and caves by the population of each county
    analysis_df['Missing_per_100k'] = (analysis_df['Missing_Count'] / analysis_df[2022]) * 100000
    analysis_df['Caves_per_100k'] = (analysis_df['Cave_Count'] / analysis_df[2022]) * 100000

    return analysis_df

def missing_per_pop_by_caves(analysis_df):
    # Separate counties with and without caves
    with_caves = analysis_df[analysis_df.loc[:, 'Caves_per_100k'] > 0]
    without_caves = analysis_df[analysis_df.loc[:, 'Caves_per_100k'] <= 0]

    # For those with caves, dynamically create bins based on their distribution
    # Example: using percentiles that split the data by 50%
    bins = [-np.inf, with_caves.loc[:, 'Caves_per_100k'].quantile(0.5), np.inf]
    labels = ['Lower Half', 'Upper Half']

    with_caves.loc[:, 'Cave_Density_Category'] = pd.cut(with_caves.loc[:, 'Caves_per_100k'],
                                                        bins=bins, labels=labels)

    # Re-integrate the without_caves with a label indicating 'No Caves'
    without_caves.loc[:, 'Cave_Density_Category'] = 'No Caves'
    analysis_df = pd.concat([with_caves, without_caves])

    # Calculate average missing persons rate per 100k for each category
    avg_missing_by_density = analysis_df.groupby(
        'Cave_Density_Category')['Missing_per_100k'].mean().reset_index()

    return avg_missing_by_density
