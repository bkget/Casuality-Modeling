# Casual Inference Modeling of Breast Cancer Diagnosis
<img style = "padding-left:10%" src="https://images.medicaldaily.com/sites/medicaldaily.com/files/styles/full_breakpoints_theme_medicaldaily_desktop_1x/public/2013/11/29/breast-cancer-3d-rendering.jpg" width="200" height="200"/>


## Introduction

A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:

- “What will happen if I halve the price of my product?”
- “Which clients will pay their debts only if I call them?”

Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning.


## Project Overview

The project involves with the following points
- Read the data
- Perform exploratory analysis on it
- Extract features and scale the extracted feature
- Split the data into training and hold-out set
- Create casual graph using different technique
- Examine the model performance based on the graph


## Data

The data used for this project can be extracted from [Kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) or [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets?name=breast)


## Installation

- **The Repository**
```
git clone https://github.com/bkget/Casuality-Modeling.git
cd Casuality-Modeling
pip install -r requriements.txt
```

- **Jupyter Noteboks**
```
cd notebooks
jupyter notebook 1.EDA
```
