"""H"""
# 0) Read the dataset into pandas dataframe paying attention to file delimeter.
# 1) Identify the variables inside the dataset
# 2) Investigate the correlation between the variables
# 3) Choose appropriate variables to predict company profit. Justify your choice.
# 4) Plot explanatory variables against profit in order to confirm (close to) linear dependence
# 5) Form training and testing data (80 /20 split)
# 6) Train linear regression model with training data
# 7) Compute RMSE and R2 values for training and testing data separately

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv("50_Startups.csv", delimiter=',')
print(data.head())
"""Muuttujina ovat R&D Spend, Administration, Marketing Spend, state, Profit"""
sns.heatmap(data=data.corr().round(2).abs(), annot=True)
plt.show()
"""korrelaatio Profitin kanssa sironta kuviona"""
plt.subplot(1, 2, 1)
plt.scatter(data['R&D Spend'], data['Profit'], edgecolors='red')
plt.title('korrelaatio Profitin kanssa sironta kuviona')
plt.xlabel("R&D Spend")
plt.ylabel("Profit")
plt.subplot(1, 2, 2)
plt.scatter(data['Marketing Spend'], data['Profit'])
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.show()

plt.plot()
plt.scatter(data['R&D Spend'], data['Marketing Spend'], edgecolors='black')
plt.title('Keskinäinen korrelaatio sirontakuviona')
plt.xlabel("R&D Spend")
plt.ylabel("Marketing Spend")
plt.show()
"""Vaikka Selittävät muuttujat korreloivat voimakkaasti toistensa kanssa niin korreloivat ne vielä voimakkaammin"""
""" Profitin kanssa """

X = pd.DataFrame(data[['R&D Spend', 'Marketing Spend']], columns=['R&D Spend', 'Marketing Spend'])
y = data['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""Splitataan 80/20 suhteella opetus- ja testi dataan"""
print(X_train.shape)  # vilkaistaan että splitti on onnistunut
print(X_test.shape)

"""Tehdään Lineaarinen regressio opetus datalle"""
lr = LinearRegression()
lr.fit(X_train, y_train)
y_train_predict = lr.predict(X_train)
"""Tässä Evaluoinnit ensin opetus datalle ja sitten testi datalle arvot heittelevät hieman, """
"""kun jätin splitistä randomstate :in pois"""
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)
print('RMSE', rmse, 'R2', r2)

y_test_predict = lr.predict(X_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2 = r2_score(y_test, y_test_predict)
print('RMSE_Test', rmse, 'R2_test', r2)
