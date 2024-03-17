# **SIADS 643 Week 2 Converting Jupyter Notebook to Script**
The task for this assignment was to convert an old Jupyter Notebook to a python script.

## Description
 For this task I have selected one old file that was a part of the Cave Data v/s Missing People analysis. This project was to understand if there exists any relationship between the people that go missing and the cave densities in counties in the United States (To limit the scope due to time restrictions only the US was selected for this).

## Data Files
All the files required have been put under the [data_files](data_files/.) folder. We have used four different datasets for this analysis - 

1. [Missing People](data_files/missing_person_output.csv) dataset ([Source](https://www.namus.gov/MissingPersons/Search#/results))
2. [Caves](data_files/caves_output.csv) dataset ([Source](https://cave-exploring.com/index.php/long-and-deep-caves-of-the-world/usa-long-caves-by-state/))
3. [Population by Counties](data_files/county_pop.xlsx) dataset ([Source](https://www2.census.gov/programs-surveys/popest/tables/2020-2023/counties/totals/co-est2023-pop.xlsx))
4. [US States Abbreviations and Full Forms](data_files/us_states.csv) dataset (Generated Manually)

These were obtained by scrapping data off of the web. The code for the scrapping (using BeautifulSoup in Python) is not included in this repository as it is not relevant to the task of this week's assignment.

To know more about these file contents please go to the [data_files](data_files/.) folder and see the [README.md](data_files/README.md) file there. 

## File Descriptions
### [main.py](main.py)
This is the main file.

``` bash
python main.py "data_files/missing_person_output.csv" "data_files/caves_output.csv" "data_files/county_pop.xlsx"
```

### [missing_persons.py](missing_persons.py)
This is the missing persons file.

### [caves.py](caves.py)
This is the caves file.

### [county_population.py](county_population.py)
This is the county population file.

### [data_per_county.py](data_per_county.py)
This is the data per county file.

### [graphs.py](graphs.py)
This is the graphs file.

### [Data_analysis.ipynb](Data_analysis.ipynb)
This is the original jupyter notebook that contains all the code work done in the project.

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
