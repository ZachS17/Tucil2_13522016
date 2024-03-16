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

def displayarraypoint(arr):
    for i in range (len(arr)):
        displaypoint(arr[i])

# beda metode dalam saja
# dipisah sebanyak n
# parameter array of control points
def greedyqcgen(narray,i,n,points,display): # points,display declare dari luar fungsi kosong dan akan diisi
    if (n != 0 and i != n):  
        if (i == n-1):
            # cari titik untuk panggil rekursi
            while (len(narray) != 1): # masih > 1 titik
                for i in range (0,len(narray)-1):
                    temp = midpoint(narray[i],narray[i+1]) # midpoint antar indeks array
                    points.append(temp) # list point
                    narray[i] = temp # perbaiki nilai
                narray.pop() # keluarin terakhir (g dianggap lagi)
            display.append(narray[0])
            points.append(narray[0])
            return narray[0] # nilai tengah akhir
        
        else: # sisanya hanya proses
            # untuk panggil rekursi dibagi 2, kiri dan kanan
            banyaktitik = len(narray)
            arraykiri = [narray[0]]
            arraykanan = [narray[len(narray)-1]]
            while (len(narray) != 1): # masih > 1 titik
                jtitik = len(narray)
                for i in range (0,len(narray)-1):
                    temp = midpoint(narray[i],narray[i+1])
                    if (jtitik % 2 == 0 and i == (jtitik//2)-1): # di tengah genap
                        arraykiri.append(midpoint(arraykiri[len(arraykiri)-1],temp))
                        arraykanan.insert(0,midpoint(arraykanan[0],temp))
                    elif (jtitik % 2 != 0 and i == (jtitik//2)-1): # di tengah kiri ganjil
                        arraykiri.append(midpoint(arraykiri[len(arraykiri)-1],temp))
                    elif (jtitik % 2 != 0 and i == (jtitik//2)+1): # di kanan tengah ganjil
                        arraykanan.insert(0,midpoint(arraykanan[0],temp))
                    elif (i < jtitik//2): # di kiri
                        arraykiri.append(temp)
                    elif (i > jtitik//2): # di kanan
                        arraykanan.insert(0,temp)
                    points.append(temp) # list pointi
                    narray[i] = temp # perbaiki nilai
                narray.pop() # keluarin nilai terakhir (g dianggap lagi)
            display.append(narray[0])
            displayarraypoint(narray)
            displayarraypoint(arraykiri)
            displayarraypoint(arraykanan)

            print("iterasi ke-",i)

            # rekursi
            left_result = greedyqcgen(arraykiri, i + 1, n, points, display)
            right_result = greedyqcgen(arraykanan, i + 1, n, points, display)
            return midpoint(left_result, right_result)

# contoh penggunaan
titik1 = Point(1,1)
titik2 = Point(2,3)
titik3 = Point(3,1)
titik4 = Point(4,2)
temp = [titik1,titik2,titik3]

points = []
display = []

greedyqcgen(temp,0,3,points,display)
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