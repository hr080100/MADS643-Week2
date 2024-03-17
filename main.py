"""
This is the main file that runs the complete pipeline.
There are no errors and should work perfectly fine in
any python environment.
"""

# Importing the required libraries.
import sys
import missing_persons as mp
import caves as ca
import county_population as co
import graphs as gp
import data_per_county as dpc

# Main function.
if __name__ == '__main__':
    # data_sets = []
    # args = dict(zip(data_sets, sys.argv))
    # print(len(sys.argv))

    # Getting the missing persons dataset.
    if len(sys.argv) > 3:
        missing_persons = mp.missing_persons(sys.argv[1])
    else:
        missing_persons = mp.missing_persons()

    # Getting the caves dataset.
    if len(sys.argv) > 3:
        caves = ca.caves(sys.argv[2])
    else:
        caves = ca.caves()

    # Getting the county populations dataset.
    if len(sys.argv) > 3:
        county_pop = co.county_pop(sys.argv[3])
    else:
        county_pop = co.county_pop()

    # Creating a countplot of the number of caves by each
    # state in the USA.
    gp.caves_by_state_countplot(caves).show()

    # Creating a countplot of the number of people gone
    # missing by year
    gp.missing_persons_by_year_countplot(missing_persons).show()

    # Creating a histplot of the number of people gone
    # missing by thier age and gender.
    gp.missing_persons_by_age_and_gender_histplot(missing_persons).show()

    # Getting analysis_df that has all the combined data
    # of missing people, county and populations.
    analysis_df = dpc.data_per_county(missing_persons, caves, county_pop)
    # Creating a scatterplot of the people missing per
    # 100,000 people (population) and the cave density per
    # 100,000 people (population).
    gp.missing_persons_per_pop_scatterplot(analysis_df).show()

    # Analysis of missing people in counties with no caves,
    # lower half and upper half based on 50% percentile.
    avg_missing_by_density = dpc.missing_per_pop_by_caves(analysis_df)
    # Creating a barplot based on the percentile above.
    gp.avg_missing_by_density_barplot(avg_missing_by_density).show()
