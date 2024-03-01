import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("data_banknote_authentication.csv")
#print(df.head())
X = df.drop('class', axis=1)
y = df['class']
X_opetus, X_testi, y_opetus, y_testi = train_test_split(X, y, test_size=0.20, random_state=20)
#print(X_opetus.shape, X_testi.shape)
# Lineaarinen ydin
lajiteltu = SVC(kernel='linear')
lajiteltu.fit(X_opetus, y_opetus)
y_arvio = lajiteltu.predict(X_testi)
# Lineaarisen ytimen Evaluointi !!
print(confusion_matrix(y_testi, y_arvio))
print(classification_report(y_testi, y_arvio))

# rbf ydin
lajiteltu = SVC(kernel='rbf')
lajiteltu.fit(X_opetus, y_opetus)
y_arvio = lajiteltu.predict(X_testi)
# Lineaarisen ytimen Evaluointi !!
print(confusion_matrix(y_testi, y_arvio))
print(classification_report(y_testi, y_arvio))

#######################################################################################################################
# Tässä tapauksessa näyttää, että säteeseen pohjautuva funktio antaa hivenen paremman tuloksen 2 meni väärin
# lineaarisella mallilla. säteeseen perustuva sai kaikki oikein
#######################################################################################################################

