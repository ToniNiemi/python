# import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
# import numpy as np


df = pd.read_csv('weight-height.csv', skiprows=0, delimiter=",")
x = 2.54*df[['Height']]
y = 0.4535923*df[['Weight']]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

X_train_norm = MinMaxScaler().fit_transform(X_train)
X_test_norm = MinMaxScaler().fit_transform(X_test)

X_train_std = StandardScaler().fit_transform(X_train)
X_test_std = StandardScaler().fit_transform(X_test)

knn = neighbors.KNeighborsRegressor(n_neighbors=5)
# orig
knn.fit(X_train, y_train)
print("R2 ", knn.score(X_test, y_test))

# min-max
knn.fit(X_train_norm, y_train)
print("R2 min-max ", knn.score(X_test_norm, y_test))

# std
knn.fit(X_train_std, y_train)
print("R2 std ", knn.score(X_test_std, y_test))  # Näyttäisi, että skaalaamisesta ei aina ole apua!
