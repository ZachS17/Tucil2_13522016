import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def midpoint(t0,t1):
    titiktengah = Point((0.5*t0.x+0.5*t1.x),(0.5*t0.y+0.5*t1.y))
    return titiktengah

# pecah jadi midpoint gabung dengan midpoint
# rekursif

# 1 kali -> pecah midpoint t0 t1 dan midpoint t1 t2 gabungin midpoint t01 t12

# iterasi semua midpoint di awal baru dipisah dan digabung
def greedyqc(t0,t1,t2,n,points,display): # points,display declare dari luar fungsi kosong dan akan diisi
    if (len(points) == 0): # masih kosong
        # inisialisasi (iterasi pertama)
        points.append(t0)
        points.append(t1)
        points.append(t2)
        t01 = midpoint(t0,t1)
        points.append(t01)
        t12 = midpoint(t1,t2)
        points.append(t12)
        t0112 = midpoint(t01,t12)
        points.append(t0112)
        display.append(t0112)

        # iterasi berikutnya
        # udah ke solve xixixi
        for i in range (1,n):
            t0prev1 = midpoint(t0,points[3+3*(i-1)])
            points.append(t0prev1)
            t2prev2 = midpoint(t2,points[4+3*(i-1)])
            points.append(t2prev2)
            tcomb = midpoint(t0prev1,t2prev2)
            points.append(tcomb)
            display.append(tcomb)