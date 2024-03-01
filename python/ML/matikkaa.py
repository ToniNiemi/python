import matplotlib.pyplot as plt
import numpy as np


A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
print('A=', A)
invA = np.linalg.inv(A)
print('invA', invA, '\n')
print((A @ invA))       # Matriisi tulo A,Ainv
print('\n')
print((invA @ A))       # Matriisi tulo ainv,A

# En saanut oikeaa tulosta en osaa laskea sitä varmaan oikein


x = np.linspace(0,5,5)
y = x * 2 + 1
y1 = x * 2 + 2
y2 = x * 2 + 3
plt.title('koulutehtävä15.5', color='red')
plt.plot(x, y, 'r', x, y1, 'b--', x, y2, 'g:')
plt.xlabel("x - akseli")
plt.ylabel("y - akseli")
plt.show()

x = np.linspace(1, 9, 9)  # Luodaan tasavälinen akseli x
y = [-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78]  # Luodaan lista y arvoista jotka oli annettu tehtävässä
plt.title('koulutehtävä 15,6')      # Annoin otsikonkin
plt.scatter(x, y, marker='+')       # Tehdään sironta kuvio ja määritetään markkeriksi +
plt.show()


koko = np.loadtxt(fname='weight-height.csv', delimiter=',', skiprows=1, usecols=(1, 2))
pituus = 2.54 * (koko[:, 0])
paino = 0.45359237 * (koko[:, 1])
print('pituuden keskiarvo ', np.mean(pituus), 'cm')
print('painon keskiarvo', np.mean(paino), 'kg')
print('pituuden mediaani', np.median(pituus), 'cm')
print('painon mediaani', np.median(paino), 'kg')
print('pituuden keskihajonta', np.std(pituus), 'cm')
print('painon keskihajonta', np.std(paino), 'kg')
print('pituuden varianssi', np.var(pituus), 'cm')
print('painon varianssi', np.var(paino), 'kg')


# tuuma=2.54cm, pauna=0.45359237 kg
print('summa on ', s)
print('sarakesumma on ', np.sum(A, axis=0))
print('rivisumma on ', np.sum(A, axis=1))
print('tulo on ', np.prod(A))
print('minimi on ', np.min(A))
print('maksimi on ', np.max(A))
print('keskiarvo on ', np.mean(A))
print('mediaani on ', np.median(A))
print('keskihajonta on ', np.std(A))
print('varianssi on ', np.var(A))
A = [[1, 2], [3, 4]]
B = [[-1, 1], [5, 7]]
DetA = (np.linalg.det(A))  # Det A
DetB = (np.linalg.det(B))  # Det B
C = np.matmul(A, B)      # Matriisi tulo AB
DetC = (np.linalg.det(C))  # Det C
print('Determinantit: A:', DetA, 'B:', DetB, ', ja Matriisitulon AB determinantti', DetC)
