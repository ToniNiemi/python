from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = np.genfromtxt('weight-height.csv', delimiter=',', skip_header=1)
xpit = data[:, 1]  # valitaan datasta arvot, jotka sijoitetaan
ypai = data[:, 2]

xpit = xpit.reshape(-1, 1)  # X pituus Muotoillaan sk learnia varten
ypai = ypai.reshape(-1, 1)  # Y paino Muotoillaan sk learnia varten

regres = LinearRegression()      # valitaan lineaarinen regressio
regres.fit(xpit, ypai)        # sovitetaan regressio

xarvo = np.full((1, 1), 0.5)    # valitaan X uudet arvot
yarvo = regres.predict(xarvo)   # jotka vastaavat y arvoja tämä siis muuttaa y arvot ennuste linjalle
yarvio = regres.predict(xpit)   # ennustetaan Y arvio

plt.scatter(xpit, ypai, marker='+')  # tehdää scatteri arvoista
plt.xlabel('pituus tuumina')
plt.ylabel('paino paunoina')
plt.plot(xpit, yarvio, color="red")  # plotataan arvio viiva

print('RMSE', np.sqrt(metrics.mean_squared_error(ypai, yarvio)), 'R2', metrics.r2_score(ypai, yarvio))
plt.show()  # yllä tulostetaan rmse ja r2 arvot
