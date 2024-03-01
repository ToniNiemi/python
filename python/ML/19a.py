"""h"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


data = load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MEDV'] = data.target
sns.heatmap(data=df.corr().round(2), annot=True)
plt.show()
"""tämä heatmappi kertoo että ptratio ja chas arvot taitavat olla ainoat jotka correloivat """
"""enemmän medv kanssa kuin rm tai lstat arvon kanssa chas vaikuttaa niin vähän että ptratio on siksi valintani"""
"""chas arvo on myös hieman hankala kun sillä on vain arvo 0 tai 1 ja se pudottaa vain halvimmat pois,"""
"""kuten alla näemme."""

plt.subplot(1, 2, 1)
plt.scatter(df['CHAS'], df['MEDV'])
plt.xlabel("CHAS")
plt.ylabel("MEDV")
plt.subplot(1, 2, 2)
plt.scatter(df['PTRATIO'], df['MEDV'])
plt.xlabel("PTRATIO")
plt.ylabel("MEDV")
plt.show()
"""Tässä alkutilanne  arvoina pelkkä rm ja lstat"""
print('Alkutilanne arvoina LSTAT ja RM')
X = pd.DataFrame(df[['LSTAT', 'RM']], columns=['LSTAT', 'RM'])
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_train_predict = lm.predict(X_train)
rmse_0 = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2_0 = r2_score(y_train, y_train_predict)
y_test_predict = lm.predict(X_test)
rmse_test_0 = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test_0 = r2_score(y_test, y_test_predict)
print('RMSE', rmse_0, 'r2', r2_0)
print('rmse_test', rmse_test_0, 'r2_test', r2_test_0)
print('Seuraava vaihe jossa lisätty PTRATIO')
lm = LinearRegression()
X = pd.DataFrame(df[['LSTAT', 'RM', 'PTRATIO']], columns=['LSTAT', 'RM', 'PTRATIO'])
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

lm.fit(X_train, y_train)
y_train_predict = lm.predict(X_train)
rmse_1 = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2_1 = r2_score(y_train, y_train_predict)
y_test_predict = lm.predict(X_test)
rmse_test_1 = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test_1 = r2_score(y_test, y_test_predict)
print('RMSE', rmse_1, 'r2', r2_1)
print('rmse_test', rmse_test_1, 'r2_test', r2_test_1)
print('Ja viimeksi Vaihe jossa on Kaikki Neljä muuttujaa RM, LSTAT, PTRATIO, CHAS')
X = pd.DataFrame(df[['LSTAT', 'RM', 'CHAS', 'PTRATIO']], columns=['LSTAT', 'RM', 'CHAS', 'PTRATIO'])
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
lm = LinearRegression()
lm.fit(X_train, y_train)
y_train_predict = lm.predict(X_train)
rmse_2 = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2_2 = r2_score(y_train, y_train_predict)
y_test_predict = lm.predict(X_test)
rmse_test_2 = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test_2 = r2_score(y_test, y_test_predict)
print('RMSE', rmse_2, 'r2', r2_2)
print('rmse_test', rmse_test_2, 'r2_test', r2_test_2)
"""Onnistuin ensin lisäämään tarkkuutta noin 3 prosenttia ja sitten vielä yhden prosentin uskoisin,"""
""" että jos olisin valinnut, muita parametreja olisin huonontanut tarkkuutta ON VÄLIÄ MITÄ VALITSEE SELITTÄJIKSI"""
