import numpy as np
from matplotlib import pyplot as plt


def noppa(n):
    """Heittää kahta 6 tahoista noppaa annetun lkm (n) varran palauttaa summan tarvitsee numpy moduulin"""
    a = (np.random.randint(1, 7, n))
    b = (np.random.randint(1, 7, n))
    c = a + b
    return c


def main():
    i = 0
    for i in range(9):
        if i == 0:
            n = 500
        elif i == 1:
            n = 1000
        elif i == 2:
            n = 2000
        elif i == 3:
            n = 5000
        elif i == 4:
            n = 10000
        elif i == 5:
            n = 15000
        elif i == 6:
            n = 20000
        elif i == 7:
            n = 50000
        elif i == 8:
            n = 100000

        d = noppa(n)
        a, b = np.histogram(d, range(2, 14))
        plt.bar(b[:-1], a / n)
        plt.title(n)
        plt.show()
        i += 1


if __name__ == "__main__":
    main()
