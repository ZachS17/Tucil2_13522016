import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def quadraticpoints(t0, t1, t2, i):
    # Interpolasi t0 dan t1
    x1 = t0.x + i * (t1.x - t0.x)
    y1 = t0.y + i * (t1.y - t0.y)

    # Interpolasi t1 dan t2
    x2 = t1.x + i * (t2.x - t1.x)
    y2 = t1.y + i * (t2.y - t1.y)

    # Interpolasi 1 dan 2
    xtemp = x1 + i * (x2 - x1)
    ytemp = y1 + i * (y2 - y1)

    return xtemp, ytemp

def quadraticcurve(t0, t1, t2):
    x = []
    y = []
    for i in np.arange(0.0, 1.001, 0.001): # iterasi float
        xtemp, ytemp = quadraticpoints(t0, t1, t2, i)
        x.append(xtemp)
        y.append(ytemp)
    return x, y

def cubicpoints(t0, t1, t2, t3, i):
    # Interpolasi t0 dan t1
    x1 = t0.x + i * (t1.x - t0.x)
    y1 = t0.y + i * (t1.y - t0.y)

    # Interpolasi t1 dan t2
    x2 = t1.x + i * (t2.x - t1.x)
    y2 = t1.y + i * (t2.y - t1.y)

    # Interpolasi t2 dan t3
    x3 = t2.x + i * (t3.x - t2.x)
    y3 = t2.y + i * (t3.y - t2.y)

    # Interpolasi 1 dan 2
    x12 = x1 + i * (x2 - x1)
    y12 = y1 + i * (y2 - y1)

    # Interpolasi 2 dan 3
    x23 = x2 + i * (x3 - x2)
    y23 = y2 + i * (y3 - y2)

    # Interpolasi Akhir (12 dan 23)
    xtemp = x12 + i * (x23-x12)
    ytemp = y12 + i * (y23-y12)

    return xtemp, ytemp

def cubiccurve(t0, t1, t2, t3):
    x = []
    y = []
    for i in np.arange(0.0, 1.001, 0.001): # iterasi float
        xtemp, ytemp = cubicpoints(t0, t1, t2, t3, i)
        x.append(xtemp)
        y.append(ytemp)
    return x, y

# Contoh Penggunaan
titik1 = Point(0, -3)
titik2 = Point(-5, 0)
titik3 = Point(10, 10)
titik4 = Point(-15,-5)
x, y = quadraticcurve(titik1, titik2, titik3)
x, y = cubiccurve(titik1,titik2,titik3,titik4)
plt.scatter(x, y, color='blue', marker='.')

# Hilangkan sumbu x dan y
plt.xticks([])  
plt.yticks([]) 

# Tampilan
plt.show()
