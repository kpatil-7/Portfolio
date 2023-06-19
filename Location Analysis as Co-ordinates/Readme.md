# Location Biases on Fake News Twitter Datasets

This repository contains research findings on location biases in fake news Twitter datasets. The dataset used in this research is obtained from Prof. Kai Shu of Illinois Tech. The dataset consists of celebrity gossip news and political gossip news.

## Research Objective

The objective of this research is to investigate location biases in fake news tweets. The research explores two aspects of location:

1. **Location-based Fake News Distribution**: The research examines the distribution of fake news based on the geographical coordinates associated with tweets. It analyzes the amount of fake news originating from different locations.

2. **Location Mention and Fake News**: The research explores the correlation between the mention of location in tweets and the likelihood of the tweet being fake. It investigates whether the presence of location information in a tweet can be an indicator of fake news.

## Methodology and Findings

The research employs two approaches to analyze the location biases in fake news:

1. **Geographical Coordinates**: The study analyzes the distribution of fake news based on the geographical coordinates of the tweets. It investigates if certain locations are more prone to generating fake news. The findings suggest the presence of location biases in fake news distribution, although the biases are not statistically significant.

2. **BERT and NER-BERT**: The research applies BERT (Bidirectional Encoder Representations from Transformers) and NER-BERT (Named Entity Recognition BERT) models to identify fake tweets when the location is hidden. The models are trained on the dataset to predict the likelihood of a tweet being fake without explicitly mentioning the location. The study compares the performance of these models in identifying fake news and assesses their effectiveness in mitigating location biases. The findings indicate that the models show promising results in identifying fake tweets, even when location information is concealed.

The research contributes to a better understanding of location biases in fake news dissemination and explores the potential of machine learning models in detecting fake news without relying on explicit location mentions.

## Repository Structure

- `data/`: This directory contains the dataset obtained from Prof. Kai Shu of Illinois Tech. The dataset consists of celebrity gossip news and political gossip news tweets.

- `notebooks/`: This directory includes Jupyter notebooks detailing the research methodology, data analysis, and model training. The notebooks provide step-by-step explanations of the experiments conducted and the results obtained.

- `results/`: This directory contains the research findings, including statistical analyses, visualizations, and conclusions drawn from the experiments.

## Citation

If you use this research or the dataset provided by Prof. Kai Shu of Illinois Tech, please cite the appropriate sources and give credit to the original authors.

## Contributions

Contributions to this research project are welcome. If you have any suggestions, improvements, or additional findings related to location biases in fake news Twitter datasets, please open an issue or submit a pull request on the GitHub repository.

## License

The research findings and code in this repository are licensed under the [MIT License](LICENSE). Feel free to use and modify them for academic or research purposes.

