#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:15:21 2022

@author: Jocelyne Horanituze
"""

import pandas as pd
import numpy as np

df = pd.read_csv('eda.csv')

#choose relevant columns
df.columns

df_model = df[['work_year', 'experience_level', 'employment_type',
               'salary_in_usd', 'remote_ratio', 'company_size', 'job_simp',
               'location_simp','residence_simp']]

# dummy variable for our categorical variables
df_dum = pd.get_dummies(df_model)
#train test split
from sklearn.model_selection import train_test_split
X = df_dum.drop(['salary_in_usd'], axis=1)
y = df_dum['salary_in_usd']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#multiple linear regression
#from scipy import stats
import statsmodels.api as sm
#from statsmodels.formula.api import ols

X_sm = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

#lm = LinearRegression(normalize = True)
lm = LinearRegression()
lm.fit(X_train,y_train)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))

from sklearn.linear_model import Ridge
rr = Ridge(alpha=0.01)
rr.fit(X_train, y_train) 
np.mean(cross_val_score(rr,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))
rr.score(X_train, y_train)

#LASSO regression 
lasso = Lasso()
lasso.fit(X_train, y_train)
np.mean(cross_val_score(lasso,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))
lasso.score(X_train, y_train)

#Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
np.mean(cross_val_score(rf,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))

#tune models using GridSearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse', 'mae'), 'max_features': ('auto', 'sqrt', 'log2')}
gs = GridSearchCV(rf, parameters, scoring = 'neg_mean_absolute_error', cv=3)
gs.fit(X_train, y_train)

gs.best_score_
gs.best_estimator_
#RandomForestRegressor(criterion='mae', max_features='log2', n_estimators=160)
#test ensembles
tpred_lm = lm.predict(X_test)
tpred_lasso = lasso.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lasso)
mean_absolute_error(y_test, tpred_rf)

#combine the 2 best models
mean_absolute_error(y_test, (tpred_lasso+tpred_rf)/2)

#Productionize the model in FLASK

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )


file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
model.predict(X_test.iloc[1,:].values.reshape(1, -1))
