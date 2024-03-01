# 1) Read data into pandas dataframe
# 2) Setup multiple regression X and y to predict 'mpg' of cars using all the variables except 'mpg', 'name'and 'origin'
# 3) Split data into training and testing sets (80 /20 split)
# 4) Implement both ridge regression and LASSO regression using several values for alpha.
# 5) Search optimal value for alpha (in terms of R2 score) by fitting the models with training data and computing
#    the score using testing data
# 6) Plot the R2 scores for both regressors as functions of alpha
# 7) Identify, as accurately as you can, the value for alpha which gives the best score

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


dat = pd.read_csv('Auto.csv')
y = dat[['mpg']]
X = dat[['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#################################################################
# Ridge regressio  92.06
#################################################################
alphas = np.linspace(92, 92.30, 20)                             #
r2values = []                                                   #
for alp in alphas:                                              #
    regr = linear_model.Ridge(alpha=alp)                        #
    regr.fit(X_train, y_train)                                  #
    r2_test = r2_score(y_test, regr.predict(X_test))            #
    r2values.append(r2_test)                                    #
plt.plot(alphas, r2values)                                      #
plt.title('ridge regression')                                   #
plt.show()                                                      #
print('paras arvo oli 92.06')                                   #
#################################################################
# Lasso Regressio 0.2685
#################################################################
alphas = np.linspace(0.2, 0.5, 50)                              #
scores = []                                                     #
for alp in alphas:                                              #
    lasso = linear_model.Lasso(alpha=alp)                       #
    lasso.fit(X_train, y_train)                                 #
    sco = lasso.score(X_test, y_test)                           #
    scores.append(sco)                                          #
plt.plot(alphas, scores)                                        #
plt.title('Lasso regression')                                   #
plt.show()                                                      #
Print('paras arvo oli 0.2685')                                  #
#################################################################

