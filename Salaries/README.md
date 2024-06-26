# DATA SCIENCE SALARY ESTIMATOR 

* Created a tool that estimates data science salaries (MAE ~ $ 29K) to help data scientists negotiate their income when they get a job.
* Optimized Linear, Lasso, Ridge, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used
* **Dataset and Description:** https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries
* **Python Version:** 3.7
* **Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* **Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
* **YouTube Project Walk-Through:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Data Cleaning
I clean up data so that it was usable for our model. I made the following changes and created the following variables:

* Removed unnamed:0, salary, salary_currency columns 
* Added a column for simplified job title
* Added a column for simplified company location
* Added a column for simplified employee residence

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights.
![countries](https://user-images.githubusercontent.com/44282495/208831528-79e98b40-3972-4e97-ac34-5e40bb42bb8d.png)
![DS_roles](https://user-images.githubusercontent.com/44282495/208831685-5a818266-5496-4c2a-993d-934d93e7cb98.png)
![residence](https://user-images.githubusercontent.com/44282495/208831702-f11ecce3-04b9-4787-bfad-c958306e6806.png)
<img width="633" alt="salary_year" src="https://user-images.githubusercontent.com/44282495/208831727-6c9ef283-5ec9-47b5-a56a-c98f470b9e79.png">
<img width="680" alt="data" src="https://user-images.githubusercontent.com/44282495/208831668-7d749baf-d2e6-4b9c-971f-5160cfaed0d8.png">

## Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried four different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried four different models:

* Multiple Linear Regression – Baseline for the model
* Lasso Regression
* Ridge Regression
* Random Forest 


## Model Performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

* Random Forest : MAE = 29215.66
* Linear Regression: MAE = 30841.95
* Ridge Regression: MAE = 30838.10
* LASSO Regression: MAE = 30830.94

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.


