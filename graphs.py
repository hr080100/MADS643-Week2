"""
This file is used for generating final graphs
for the analysis of the project. There are functions
that when called generate a plot.
"""

# Importing the required libraries.
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a countplot of the number of caves by each
# state in the USA.
def caves_by_state_countplot(caves_data):
    """
    This function generates a countplot based
    on the number of caves in each state of the USA.
    """
    plt.figure(figsize=(15,6))
    sns.countplot(data=caves_data, x='State')
    plt.xticks(rotation=45)
    plt.title('Number of Caves by State')
    return plt

# Creating a countplot of the number of people gone
# missing by year
def missing_persons_by_year_countplot(missing_persons_data):
    """
    This function generates a countplot of the
    missing people every year.
    """
    missing_persons_data['Year'] = missing_persons_data['DLC'].dt.year
    plt.figure(figsize=(10,6))
    sns.countplot(data=missing_persons_data, x='Year')
    plt.title('Missing Persons Cases Over Time')
    return plt

# Creating a histplot of the number of people gone
# missing by thier age and gender.
def missing_persons_by_age_and_gender_histplot(missing_persons):
    """
    This function generates a histplot of the
    missing persons by distinguishing on the
    gender and age of the missing people.
    """
    sns.histplot(data=missing_persons, x='Age', hue='Gender', bins=30, kde=True)
    plt.title('Distribution of Missing Persons by Age and Gender')
    return plt

# Creating a scatterplot of the people missing per
# 100,000 people (population) and the cave density per
# 100,000 people (population).
def missing_persons_per_pop_scatterplot(analysis_df):
    """
    This function creates a scatterplot of the
    density of people going missing per 100,000
    people and the caves densities per 100,000
    people.
    """
    sns.scatterplot(data=analysis_df, x='Caves_per_100k', y='Missing_per_100k')
    plt.title('Missing Persons vs. Cave Density per 100k Population')
    plt.xlabel('Caves per 100k Population')
    plt.ylabel('Missing Persons per 100k Population')
    return plt

# Creating a barplot based on the percentile.
def avg_missing_by_density_barplot(avg_missing_by_density):
    """
    This function generates a barplot based on the percentile
    of caves dencities and the people going missing
    in the counties with no caves, lower than 50% threshold of
    the caves and higher than 50% threshold of the caves.
    """
    sns.barplot(data=avg_missing_by_density, x='Cave_Density_Category', y='Missing_per_100k')
    plt.title('Average Missing Persons Rate per 100k by Cave Density Category')
    plt.xlabel('Cave Density Category')
    plt.ylabel('Average Missing Persons Rate per 100k')
    return plt
