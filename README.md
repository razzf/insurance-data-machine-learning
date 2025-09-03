# Project Title: Supervised Machine Learning Fundamentals - Explanatory and Predictive Modeling of Travel Insurance Data

## Project Overview
This project analyzes travel insurance data to understand the factors influencing the purchase of a **Travel Insurance Package**. It involves data preprocessing, exploratory data analysis (EDA), statistical modeling, and machine learning techniques to develop predictive models for this classification task.

## Objectives
The primary objective is to identify business opportunities for the travel insurance package, specifically targeting customers who are likely to purchase the product.

Moreover, the project aims to:
- Explore the relationships between customer features.
- Perform statistical inference on the customer dataset.
- Identify the most significant predictors of Travel Insurance Package purchase.
- Build multiple machine learning models to provide the best prediction for Travel Insurance Package purchase.

## Key Insights
- The most important features to predict Travel Insurance Package purchase are especially *Income* and if a customer *ever travelled abroad* before.
- But also *Age*, number of *family members*, and if a customer is a *frequent flyer* are important features, as discovered in correlation analysis and logistic regression analysis.
- The *Random Forest with hypertuning* performed the best among the tested and validated machine learning models
- This model could reach on a hold-out test data set an *accuracy* score of 0.844 and a very impressive *precision* score of 0.988.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Directory Structure](#directory-structure)
- [Requirements](#requirements)
- [Notebook Overview](#notebook-overview)

## Installation

To set up this project locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TuringCollegeSubmissions/jwerne-DS.v2.5.3.1.5.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd jwerne-DS.v2.5.3.1.5
   ```
3. **Install required packages**:
   Ensure Python is installed and use the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Open the notebook in Jupyter or JupyterLab to explore the analysis. Execute the cells sequentially to understand the workflow, from data exploration to model building and evaluation.


## Data

The dataset is located in the `/data` directory. It is originally derived from [Kaggle](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data). The data set reflects a collection of customer data from a Tour & Travels Company which is offering a Travel Insurance Package. The insurance was offered to some of the customers in **2019**. The given data has been extracted from the performance/sales of the package during that period. It contains data of 1.987 customers for 8 features (e.g. Age, Employment, Type, Income, if Customer has ever travelled/ is a frequently flyer, etc.) and one variable containing information if Travel Insurance Package was bought. The data origins are unknown. 

## Directory Structure

```
project-root/
├── custom_modules/
│   ├── plotting.py                    # Module for plotting
│   └── stat_calculations.py           # Module for calculations
├── data/
│   └── TravelInsurancePrediction.csv  # Dataset for analysis
├── notebook/
│   └── data_analysis_and_modeling.ipynb   # Jupyter notebook for analysis
├── requirements.txt                   # Package dependencies
└── README.md                          # Project documentation
```


## Requirements

The `requirements.txt` file lists all Python dependencies. Install them using the command provided above.

## Notebook Overview

The notebook includes the following sections:
1. **Introduction**  
2. **Project Discovery**  
3. **Objectives**
4. **Problem Definition**
5. **Data acquisition and preparation**
6. **Data cleaning**
7. **Exploratory Data Analysis**  
8. **Statistical Inference, modeling and evaluation**   
9. **Model Learning modeling and evaluation**  
10. **Suggestions for improvement**  