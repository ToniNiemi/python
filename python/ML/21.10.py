import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('suv.csv')
# print(df.head(), '\n', df.shape)
y = df[['Purchased']]
X = df[['Age', 'EstimatedSalary']]
# print(X.head())
# splitataan
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)
# Skaalataan
X_train_std = StandardScaler().fit_transform(X_train)
X_test_std = StandardScaler().fit_transform(X_test)
# Luokitellaan entropy
luokittelija = DecisionTreeClassifier(criterion="entropy")
luokittelija.fit(X_train_std, y_train)
y_arvio = luokittelija.predict(X_test_std)
# arvioidaan
print(confusion_matrix(y_test, y_arvio))
print(classification_report(y_test, y_arvio))

# Luokitellaan gini
luokittelija = DecisionTreeClassifier(criterion="gini")
luokittelija.fit(X_train_std, y_train)
y_arvio = luokittelija.predict(X_test_std)
# arvioidaan
print(confusion_matrix(y_test, y_arvio))
print(classification_report(y_test, y_arvio))

# #####################################################################################################################
# Enropialla saatiin parempi tarkkuus vain 7 väärin kun taas Ginillä meni väärin 9.
# #####################################################################################################################
