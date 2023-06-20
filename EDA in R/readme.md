# Customer Data Analysis using R

This repository contains R code for analyzing customer data and generating visualizations. The code explores various aspects of the customer dataset and creates informative plots to gain insights into customer demographics and spending behavior.

## Dataset

The dataset (`Mall_Customers.csv`) is a CSV file that contains information about customers of a shopping mall. It includes variables such as age, annual income, and spending score. The Dataset was procured from Kaggle

## Analysis and Visualizations

The R script `analysis.R` performs the following operations on the customer dataset:

- Loading the dataset into R
- Exploring the structure of the dataset using `str()`
- Displaying the column names using `names()`
- Previewing the first few rows of the dataset using `head()`
- Computing summary statistics for the age, annual income, and spending score variables using `summary()`
- Computing the standard deviation for the age and annual income variables using `sd()`
- Creating visualizations to understand the data, including:

  - Bar plot to compare the count of customers by gender
  - Histograms to show the distribution of age and annual income
  - Box plots for descriptive analysis of age and spending score
  - Density plot with polygon for the density estimation of annual income
  - Box plot for descriptive analysis of spending score
  - Histogram for the distribution of spending score

Feel free to modify the code and dataset according to your specific needs and requirements. You can further enhance the analysis by adding additional visualizations or performing more in-depth statistical analysis.

## Instructions

1. Install R and any required packages mentioned in the code.
2. Clone this repository to your local machine.
3. Place the dataset (`Mall_Customers.csv`) in the same directory as the R script.
4. Run the `analysis.R` script to perform the data analysis and generate the visualizations.
5. Explore the generated plots and gain insights into the customer data.

Make sure to customize the visualizations, titles, and labels as per your preference to effectively communicate the findings from the customer data analysis.
