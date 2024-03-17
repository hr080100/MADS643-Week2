"""
This file is used for generating final graphs
for the analysis of the project. There are functions
that when called generate a plot.
"""

# Importing the required libraries.
import matplotlib.pyplot as plt
import seaborn as sns

def caves_by_state_countplot(caves_data):
    plt.figure(figsize=(15,6))
    sns.countplot(data=caves_data, x='State')
    plt.xticks(rotation=45)
    plt.title('Number of Caves by State')
    return plt

def missing_persons_by_year_countplot(missing_persons_data):
    missing_persons_data['Year'] = missing_persons_data['DLC'].dt.year
    plt.figure(figsize=(10,6))
    sns.countplot(data=missing_persons_data, x='Year')
    plt.title('Missing Persons Cases Over Time')
    return plt

def missing_persons_by_age_and_gender_histplot(missing_persons):
    sns.histplot(data=missing_persons, x='Age', hue='Gender', bins=30, kde=True)
    plt.title('Distribution of Missing Persons by Age and Gender')
    return plt

def missing_persons_per_pop_scatterplot(analysis_df):
    sns.scatterplot(data=analysis_df, x='Caves_per_100k', y='Missing_per_100k')
    plt.title('Missing Persons vs. Cave Density per 100k Population')
    plt.xlabel('Caves per 100k Population')
    plt.ylabel('Missing Persons per 100k Population')
    return plt

def avg_missing_by_density_barplot(avg_missing_by_density):
    sns.barplot(data=avg_missing_by_density, x='Cave_Density_Category', y='Missing_per_100k')
    plt.title('Average Missing Persons Rate per 100k by Cave Density Category')
    plt.xlabel('Cave Density Category')
    plt.ylabel('Average Missing Persons Rate per 100k')
    return plt
