import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# interpolasi

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

# rumus spek
def spekqp(t0, t1, t2, i):
    # semacam persentase koordinat
    q0 = Point((1-i)*t0.x + i*t1.x, (1-i)*t0.y + i*t1.y)
    q1 = Point((1-i)*t1.x + i*t2.x, (1-i)*t1.y + i*t2.y)
    final = Point((1-i)*q0.x + i*q1.x, (1-i)*q0.y + i*q1.y)
    return final

def spekqc(t0, t1, t2):
    x = []
    y = []
    for i in np.arange(0.0, 1.001, 0.001):
        xtemp = spekqp(t0, t1, t2, i).x
        ytemp = spekqp(t0, t1, t2, i).y
        x.append(xtemp)
        y.append(ytemp)
    return x, y

# titik tengah

# iterasi 1 -> tengah t0,t1 tengah t1,t2 tengah t01,t12
# iterasi 2 -> tengah t0,t01 tengah t1,t12 tengah t001,t112
# iterasi 3

# alternatif passing 
# nilai (0,5,0,25,dll) point tetap sama tapi nilainya yang berbeda 
# atau passing titik dari array yang ada
def threelastelements(array):
    return array[-3],array[-2],array[-1]

def fourusedelements(array):
    return array[-6],array[-4],array[-3],array[-1]

def midpoint(t0,t1):
    titiktengah = Point((0.5*t0.x+0.5*t1.x),(0.5*t0.y+0.5*t1.y))
    return titiktengah

def midqp(t0,t1,t2,points,display):
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
    elif (len(points) == 6): # isinya 3 -> iterasi kedua -> akses 3 elemen terakhir array
        # ambil 3 elemen
        prev1,prev2,prevcomb = threelastelements(points)

        # titik tambahan pertama
        t0prev1 = midpoint(t0,prev1)
        tprev1prevcomb = midpoint(prev1,prevcomb)
        tcomb1 = midpoint(t0prev1,tprev1prevcomb)
        points.append(t0prev1)
        points.append(tprev1prevcomb)
        points.append(tcomb1)

        # masukkin display
        display.append(tcomb1)

        # titik tambahan kedua
        t2prev2 = midpoint(t2,prev2)
        tprev2prevcomb = midpoint(prev2,prevcomb)
        tcomb2 = midpoint(t2prev2,tprev2prevcomb)
        points.append(t2prev2)
        points.append(tprev2prevcomb)
        points.append(tcomb2)

        # masukkin display
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

        # masukkin display
        display.append(tcomb2)

# pertama : midpoint t0 t1 midpoint t1 t2 midpoint t01 t12 -> t01,t12,t0112 append
# ada 3 elemen baru untuk dipakai
# kedua : midpoint t0 t01 (hasil t0 dan gabungan pertama) midpoint t01 t0112 (gabungan pertama dan gabungan ketiga) midpoint t001 t010112 (gabungan saat ini)
    # DAN midpoint t2 t12 (hasil t2 dan gabungan kedua) midpoint t12 t0112 (gabungan kedua dan gabungan ketiga) midpoint t212 t120112 (gabungan saat ini)
# ada 6 elemen baru untuk dipakai
# ketiga : midpoint t0 t001 (hasil t0 dan gabungan pertama) midpoint t001 t001010112 (gabungan pertama dan ketiga) midpoint (gabungan saat ini)
    # DAN midpoint t2 t212 (hasil t2 dan gabungan keempat) midpoint t212 ... (gabungan keempat dan keenam) midpoint (gabungan saat ini)
# pertama beda dengan kedua
# kedua sama dengan selanjutnya
        
# t0,t1,t2 tidak apa-apain (konstan)

# i untuk berapa kali dibagi 2
def midqc(t0,t1,t2,i):
    points = []
    display = []
    for i in range (0,i):
        midqp(t0,t1,t2,points,display)
    return points,display

# contoh penggunaan
titik1 = Point(1,1)
titik2 = Point(2,3)
titik3 = Point(3,1)

allpoints,display = midqc(titik1,titik2,titik3,100)
# for i in range (0,len(temp)):
#     print(temp[i].x)
#     print(temp[i].y)
x_coordinates = [point.x for point in display]
y_coordinates = [point.y for point in display]

# Plot the curve
plt.scatter(x_coordinates, y_coordinates, label='Points', color='blue', marker='.')

# Display the plot
plt.show()
