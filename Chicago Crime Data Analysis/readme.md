This repository contains code for identifying and locating crimes in Chicago using Python. 
## Dataset

The code assumes the availability of a dataset for training and testing the image classification model. In this example, the dataset is sourced from the following CSV files:

- Chicago_Crimes_2001_to_2004.csv
- Chicago_Crimes_2005_to_2007.csv
- Chicago_Crimes_2008_to_2011.csv
- Chicago_Crimes_2012_to_2017.csv

Make sure to replace these filenames with your own dataset files or modify the code accordingly to load your dataset.

## Dependencies

The following libraries are required to run the code:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- geopandas

You can install these dependencies using pip:

```shell
pip install pandas numpy matplotlib seaborn scikit-learn geopandas
Code Overview
The code performs the following tasks:

Imports the necessary libraries and sets up the plotting environment.
Loads the dataset from the CSV files into separate DataFrames for each time period.
Performs exploratory data analysis (EDA) on the dataset.
Preprocesses the dataset by dropping duplicates and handling missing values.
Visualizes the dataset using bar plots and histograms.
Performs geospatial analysis using the GeoPandas library.
Plots the geospatial data on a map.
Feel free to modify the code to suit your specific requirements.
