import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Get summary statistics of numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualize the distribution of the target variable (tip)
sns.histplot(data=df, x='tip')
plt.xlabel('Tip Amount')
plt.ylabel('Count')
plt.title('Distribution of Tip Amount')
plt.show()

# Visualize the relationship between numerical features and the target variable
sns.pairplot(data=df, vars=['total_bill', 'size', 'tip'])
plt.show()

# Visualize the relationship between categorical features and the target variable
sns.boxplot(data=df, x='day', y='tip', hue='smoker')
plt.xlabel('Day')
plt.ylabel('Tip Amount')
plt.title('Tip Amount by Day and Smoker')
plt.show()

sns.boxplot(data=df, x='sex', y='tip', hue='time')
plt.xlabel('Sex')
plt.ylabel('Tip Amount')
plt.title('Tip Amount by Sex and Time')
plt.show()