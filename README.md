<div style="margin:0 auto;">
  <a href="https://github.com/bkget/Causal-Inference-Modeling"><img src="https://img.shields.io/github/forks/bkget/Causal-Inference-Modeling" alt="Forks Badge"/></a>
  <a "https://github.com/bkget/Causal-Inference-Modeling/pulls"><img src="https://img.shields.io/github/issues-pr/bkget/Causal-Inference-Modeling" alt="Pull Requests Badge"/></a>
  <a href="https://github.com/bkget/Causal-Inference-Modeling/issues"><img src="https://img.shields.io/github/issues/bkget/Causal-Inference-Modeling" alt="Issues Badge"/></a>
  <a href="https://github.com/bkget/Causal-Inference-Modeling/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/bkget/Causal-Inference-Modeling?color=2b9348"></a>
  <a href="https://github.com/bkget/Causal-Inference-Modeling/blob/main/LICENSE"><img src="https://img.shields.io/github/license/bkget/Causal-Inference-Modeling?color=2b9348" alt="License Badge"/></a>
  </div>
</br>
# Causal Inference Modeling of Breast Cancer Diagnosis 
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
git clone https://github.com/bkget/Causal-Inference-Modeling.git
cd Causal-Inference-Modeling
pip install -r requriements.txt
```

- **Jupyter Noteboks**
```
cd notebooks
jupyter notebook 1.EDA
```
