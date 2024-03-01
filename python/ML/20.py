import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

df1 = pd.read_csv('bank.csv', delimiter=';')

# print(df1.head())
df2 = df1[['job', 'marital', 'default', 'housing', 'poutcome']]
# print(df2.head())
# print(df2)
df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])
sea.heatmap(data=df3.corr().round=2, annot=True )
plt.show()

######################################################################################################################
print(df3)
y = df3['y']                                                    # Tämä ei mene millään oikein
X = df3[['job', 'marital', 'default', 'housing', 'poutcome']]
#######################################################################################################################






# nämä vasta suunnittelussa kun en saa järkevää dataa
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)
#
# logistic = LogisticRegression()
# logistic.fit(X_train, y_train)
# y_train_predict = logistic.predict(X_train)
#
# metrics.confusion_matrix(logistic, X_test, y_test)
# plt.show()
#
# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(X_train, y_train)
# y_predict = knn.predict(X_test)
#
# metrics._classification.classification_report(knn, X_test, y_test)
# plt.show()