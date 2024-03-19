import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def threelastelements(array):
    return array[-3],array[-2],array[-1]

def fourusedelements(array):
    return array[-6],array[-4],array[-3],array[-1]

def midpoint(t0,t1):
    titiktengah = Point((0.5*t0.x+0.5*t1.x),(0.5*t0.y+0.5*t1.y))
    return titiktengah

# alternatif : interpolasi

def qp(t0, t1, t2, i):
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

def qc(t0, t1, t2):
    x = []
    y = []
    for i in np.arange(0.0, 1.001, 0.001): # iterasi float
        xtemp, ytemp = qp(t0, t1, t2, i)
        x.append(xtemp)
        y.append(ytemp)
    return x, y

# rumus spek (utama)

def spekqp(t0, t1, t2, i):
    # semacam persentase koordinat
    q0 = Point((1-i)*t0.x + i*t1.x, (1-i)*t0.y + i*t1.y)
    q1 = Point((1-i)*t1.x + i*t2.x, (1-i)*t1.y + i*t2.y)
    final = Point((1-i)*q0.x + i*q1.x, (1-i)*q0.y + i*q1.y)
    return final

def spekqc(t0, t1, t2, i):
    itr = 1/i
    temparray = []
    for i in np.arange(0.0, 1.001, itr):
        temp = spekqp(t0,t1,t2,i)
        temparray.append(temp)
    return temparray

# alternatif : array

def brutemidqp(t0,t1,t2,points,display):
    if (len(points) == 0): # kosong -> pertama
        # masukin control point
        points.append(t0)
        points.append(t1)
        points.append(t2)

        # buat 1 titik tengah baru
        t01 = midpoint(t0,t1)
        t12 = midpoint(t1,t2)
        temp = midpoint(t01,t12)
        points.append(t01)
        points.append(t12)
        points.append(temp)

        # tambah untuk display
        display.append(temp)

        # ambil 3 elemen
        prev1,prev2,prevcomb = threelastelements(points)

        # titik tambahan pertama
        t0prev1 = midpoint(t0,prev1)
        tprev1prevcomb = midpoint(prev1,prevcomb)
        tcomb1 = midpoint(t0prev1,tprev1prevcomb)
        points.append(t0prev1)
        points.append(tprev1prevcomb)
        points.append(tcomb1)

        # masukin display
        display.append(tcomb1)

        # titik tambahan kedua
        t2prev2 = midpoint(t2,prev2)
        tprev2prevcomb = midpoint(prev2,prevcomb)
        tcomb2 = midpoint(t2prev2,tprev2prevcomb)
        points.append(t2prev2)
        points.append(tprev2prevcomb)
        points.append(tcomb2)

        # masukin display
        display.append(tcomb2)

    else: # isinya banyak -> iterasi selanjutnya -> akses 6 elemen array untuk 2 titik kontrol tambahan
        # ambil 4 elemen saja yang dibutuhkan
        prev1a,prevcomba,prev1b,prevcombb = fourusedelements(points)

        # titik tambahan pertama
        t0prev1 = midpoint(t0,prev1a)
        tprev1prevcomb = midpoint(prev1a,prevcomba)
        tcomb1 = midpoint(t0prev1,tprev1prevcomb)
        points.append(t0prev1)
        points.append(tprev1prevcomb)
        points.append(tcomb1)

        # masukin display
        display.append(tcomb1)

        # titik tambahan kedua
        t2prev2 = midpoint(t2,prev1b)
        tprev2prevcomb = midpoint(prev1b,prevcombb)
        tcomb2 = midpoint(t2prev2,tprev2prevcomb)
        points.append(t2prev2)
        points.append(tprev2prevcomb)
        points.append(tcomb2)

        # masukin display
        display.append(tcomb2)

# i untuk berapa kali dibagi 2
def brutemidqc(t0,t1,t2,i):
    points = []
    display = []
    for i in range (0,i):
        brutemidqp(t0,t1,t2,points,display)
    return points,display