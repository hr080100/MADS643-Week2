# **SIADS 643 Week 2 Converting Jupyter Notebook to Script**
The task for this assignment was to convert an old Jupyter Notebook to a python script.

## Description
This project was to understand if there exists any relationship between the people that go missing and the cave densities in counties in the United States (To limit the scope due to time restrictions only the US was selected for this). For this task I have selected one old file that was a part of this Cave Data v/s Missing People analysis.

## File Descriptions
### [main.py](main.py)
This is the main file that calls functions created in the other files and generates the grpahs in the project and stores them in the output_graphs folder. This takes three command line inputs - the paths for the data files in the following order - 

1. Missing Persons data
2. Caves data
3. County Population data

There is a default set in the files to take the path of the files as in this repository. So, the following command will work - 
```bash
python main.py
```
But, If in your local setup the files are in a different location please update the location in the following command. The command to execute this file is as follows - 
``` bash
python main.py "file path to Missing Persons data" "file path to the Caves data" "file path to the County Population data"
```
Please make sure the order of the command line input is maintained (Missing Persons data, Caves data and then County Population data).

### [missing_persons.py](missing_persons.py)
This is the missing persons file which contains the code to read the Missing Persons data file, process it into a cleaner dataset and gives a dataframe containing the processed dataset that is then used for data analysis.

### [caves.py](caves.py)
This is the caves file which contains the code to read the Caves data file, process it into a cleaner dataset and gives a dataframe containing the processed dataset that is then used for data analysis.

### [county_population.py](county_population.py)
This is the county population file which contains the code to read the County Population data file, process it into a cleaner dataset and gives a dataframe containing the processed dataset that is then used for data analysis.

### [data_per_county.py](data_per_county.py)
This is the data per county file which contains two functions - 
1. data_per_county - 

        This function takes in all the three original datasets and returns a new dataframe created by grouping the data by county and merging the datasets accordingly. It also adds two new columns that add the average of missing people and caves per 100,000 people.
2. missing_per_pop_by_caves - 

        This function takes the dataset that was generated from the above function and generates a new dataset that has values differentiating the missing people in the counties with no caves, lower number of caves than the 50% mark and higher number of caves than the 50% mark.

### [graphs.py](graphs.py)
This is the graphs file which contains five functions that generate five different graphs that are all called in the main file and the graphs are stored in the output_graphs folder.
1. caves_by_state_countplot - 

        This function generates a countplot based on the number of caves in each state of the USA.
2. missing_persons_by_year_countplot - 

        This function generates a countplot of the missing people every year.
3. missing_persons_by_age_and_gender_histplot - 

        This function generates a histplot of the missing persons by distinguishing on the gender and age of the missing people.
4. missing_persons_per_pop_scatterplot - 

        This function generates a scatterplot of the density of people going missing per 100,000 people and the caves densities per 100,000 people.
5. avg_missing_by_density_barplot - 

        This function generates a barplot based on the percentile of caves dencities and the people going missing in the counties with no caves, lower than 50% threshold of the caves and higher than 50% threshold of the caves.

### [Data_analysis.ipynb](Data_analysis.ipynb)
This is the original jupyter notebook that contains all the code work done in the project. This is the file that has been converted to the python script for this project.

### [requirements.txt](requirements.txt)
This is the requirements for the project to run correctly. For reference the code should work on any normal python environment that has these modules installed - 
1. sys
2. numpy
3. pandas
4. matplotlib
5. seaborn
6. openpyxl

But, more can be known about all the dependencies (which are usually already present in any python environment) using this requirements.txt file.

### [README.md](README.md)
This is just this very readme file containing the brief but detailed description of things in this repository.

## Data Files
All the files that have been used in this project are under the [data_files](data_files/.) folder. We have used four different datasets for this analysis - 

1. [Missing People](data_files/missing_person_output.csv) dataset ([Source](https://www.namus.gov/MissingPersons/Search#/results))
2. [Caves](data_files/caves_output.csv) dataset ([Source](https://cave-exploring.com/index.php/long-and-deep-caves-of-the-world/usa-long-caves-by-state/))
3. [Population by Counties](data_files/county_pop.xlsx) dataset ([Source](https://www2.census.gov/programs-surveys/popest/tables/2020-2023/counties/totals/co-est2023-pop.xlsx))
4. [US States Abbreviations and Full Forms](data_files/us_states.csv) dataset (Generated Manually)

These were obtained by scrapping data off of the web. The code for the scrapping (using BeautifulSoup in Python) is not included in this repository as it is not relevant to the task of this week's assignment.

To know more about these file contents please go to the [data_files](data_files/.) folder and see the [README.md](data_files/README.md) file there. 

## Output Graphs
All the graphs that have been generated in this project are stored in the [output_graphs](output_graphs/.) folder. We have generated five graphs in the project - 

1. [Caves by State Countplot](output_graphs/caves_by_state_countplot.png)
2. [Missing Persons by Year Countplot](output_graphs/missing_persons_by_year_countplot.png)
3. [Missing Persons by Age and Gender Histplot](output_graphs/missing_persons_by_age_and_gender_histplot.png)
4. [Missing Persons per 100,000 Population Scatterplot](output_graphs/missing_persons_per_pop_scatterplot.png)
5. [Average Number of People Missing by Caves Density](output_graphs/avg_missing_by_density_barplot.png)

To know more about these graphs please go to the [output_graphs](output_graphs/.) folder and see the [README.md](output_graphs/README.md) file there.