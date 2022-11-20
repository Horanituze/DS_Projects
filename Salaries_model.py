#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:15:21 2022

@author: jhoranituze2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('eda.csv')

#choose relevant columns
df.columns
#let's keep all columns for now
df_model = df

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

lm = LinearRegression()
lm.fit(X_train,y_train)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))

'''
y_pred = lm.predict(X_test)
mean_absolute_error(y_test, y_pred)

score = np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))
score
print("%0.2f accuracy with a standard deviation of %0.2f" % (score.mean(), score.std()))

'''
#LASSO regression 
lasso = Lasso(alpha = 0.99)
lasso.fit(X_train, y_train)
np.mean(cross_val_score(lasso,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lm_l = Lasso(alpha= i/100)
    error.append(np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error',cv =3)))
plt.plot(alpha, error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns= ['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]

'''
#LASSO regression (feature selection)
from sklearn.linear_model import LassoCV
lasso = LassoCV()
lasso.fit(X_train,y_train)
print('Best alpha using built-in LassoCV: %f' %lasso.alpha_)
print('Best score using built-in LassoCV: %f' %lasso.score(X,y))

coef = pd.Series(lasso.coef_, index = X.columns)
print('Lasso picked '+str(sum(coef!=0)) + ' variables and eliminated the other '+str(sum(coef==0))+' variables')

imp_coef = coef.sort_values()
plt.rcParams['figure.figsize'] = (8, 10)
imp_coef.plot(kind = 'barh')
#plt.title("Feature importance using Lasso Model")
# the selected features
kept_feat = [feature for feature, weight in zip(X.columns.values, lasso.coef_) if weight != 0]
kept_feat
'''
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
#RandomForestRegressor(criterion='mae', max_features='sqrt', n_estimators=80)
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