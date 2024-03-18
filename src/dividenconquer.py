import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def midpoint(t0,t1):
    titiktengah = Point((0.5*t0.x+0.5*t1.x),(0.5*t0.y+0.5*t1.y))
    return titiktengah

def displaypoint(t0):
    print(t0.x,t0.y)

# pecah jadi midpoint gabung dengan midpoint
# rekursif

# 1 kali -> divide midpoint t0 t1 dan midpoint t1 t2 conqure midpoint t01 t12
# 2 kali -> 

# iterasi semua midpoint di awal baru dipisah dan digabung
def greedyqc(t0,t1,t2,i,n,points,display): # points,display declare dari luar fungsi kosong dan akan diisi
    if (n != 0 and i != n):  
        if (i == n-1):
            newt1kiri = midpoint(t0,t1)
            points.append(newt1kiri)
            newt1kanan = midpoint(t1,t2)
            points.append(newt1kanan)
            newcomb = midpoint(newt1kiri,newt1kanan)
            points.append(newcomb)
            display.append(newcomb)
            return newcomb
        else: # sisanya hanya proses
            # hitung dan masukan array
            newt1kiri = midpoint(t0,t1)
            points.append(newt1kiri)
            newt1kanan = midpoint(t1,t2)
            points.append(newt1kanan)
            newcomb = midpoint(newt1kiri,newt1kanan)
            points.append(newcomb)
            display.append(newcomb)

            print("iterasi ke-",i)

            displaypoint(newt1kiri)
            displaypoint(newt1kanan)
            displaypoint(newcomb)

            displaypoint(t0)
            displaypoint(t1)
            displaypoint(t2)
            # rekursi
            left_result = greedyqc(t0, newt1kiri, newcomb, i + 1, n, points, display)
            right_result = greedyqc(newcomb, newt1kanan, t2, i + 1, n, points, display)
            return midpoint(left_result, right_result)

# contoh penggunaan
titik1 = Point(1,1)
titik2 = Point(2,3)
titik3 = Point(3,1)

points = []
display = []

greedyqc(titik1,titik2,titik3,0,1,points,display)
# for i in range (0,len(temp)):
#     print(temp[i].x)
#     print(temp[i].y)
xpoints = [point.x for point in points]
ypoints = [point.y for point in points]

xdisplay = [point.x for point in display]
ydisplay = [point.y for point in display]

# Plot the curve
plt.scatter(xdisplay, ydisplay, label='Points', color='blue', marker='.')

# Display the plot
plt.show()