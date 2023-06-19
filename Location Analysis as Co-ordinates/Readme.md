# Readme: Text Classification with Feature Engineering

## Introduction
This repository contains source code for a text classification task using feature engineering techniques. The goal is to build a machine learning model that can classify text documents into appropriate categories. In this project, we focus on implementing the Bag of Words model and applying feature engineering to improve classification accuracy.

The dataset used for this research is provided by Prof. Kai Shu of Illinois Tech. The dataset consists of two categories of gossip news: celebrity gossip and political gossip. The primary objective is to explore location biases in fake news on Twitter by considering two approaches. First, we analyze the amount of fake news originating from specific geographical coordinates. Second, we investigate the likelihood of a tweet being fake when it mentions a particular location.

## Dataset Splitting (Task 1)
The initial step of the project involves splitting the dataset into training and testing sets. The `train_test_split` function from the `sklearn.model_selection` module is used for this purpose. The code reads the 'primary.csv' file and assigns the 'text' column to variable X and the 'label' column to variable y. The data is then split into 70% for training and 30% for testing. Similarly, a secondary dataset ('secondary.csv') is split for testing purposes.

## Bag of Words Model (Task 2)
In Task 2, we implement the Bag of Words model, which converts text data into numerical representations suitable for machine learning models. The code leverages various libraries such as NLTK for text preprocessing and sklearn for feature extraction. The dataset is preprocessed using tokenization, stopword removal, stemming, and lemmatization. The CountVectorizer and TfidfTransformer are used to transform the text data into numeric features. Logistic Regression is employed as the classification model. The accuracy of the baseline model is evaluated using the accuracy_score metric.

## Baseline Model Accuracy Calculation (Task 3)
In Task 3, we calculate the accuracy of the baseline model after applying the Bag of Words model. The CountVectorizer is fitted on the training data, and a Logistic Regression model is trained on the transformed data. The model's performance is assessed by predicting labels for the testing data and calculating the accuracy using the accuracy_score function.

## Feature Engineering (Task 4)
Task 4 involves feature engineering, which aims to improve the classification performance by incorporating additional features. Three new features are defined: feature_function1, feature_function2, and feature_function3. These functions extract specific patterns or keywords from the text and return binary values indicating their presence. The new features are added to the original document representation using numpy's insert function.

## Accuracy Calculation after Feature Engineering (Task 5)
In Task 5, we evaluate the accuracy of the logistic regression model after incorporating the engineered features. The CountVectorizer is applied to the training data, and the new feature arrays are inserted into the document representation. The Logistic Regression model is then trained on the transformed data, and predictions are made for the testing data. The accuracy of the model is calculated using the accuracy_score function.

## Conclusion
In this research, we investigated location biases in fake news on Twitter using two different approaches. The findings indicate the presence of biases, although not significant. The application of feature engineering techniques, such as incorporating specific patterns and keywords, led to an improvement in the classification accuracy. By leveraging the Bag of Words model and implementing feature engineering, we demonstrated the potential to enhance the effectiveness of text classification models.

We hope that this research provides insights into the influence of location biases on fake news and serves as a valuable resource for future studies in this domain.

Please note that the code provided assumes the availability of the dataset files ('primary.csv' and 'secondary.csv') and the necessary package installations. Adjustments to file paths and installations may be required based on the specific setup.
