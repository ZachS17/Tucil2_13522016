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
    print()

# beda metode dalam saja
# dipisah sebanyak n
# parameter array of control points
def greedyqcgen(narray,indeks,n,points,display): # points,display declare dari luar fungsi kosong dan akan diisi
    print("memasuki i=",indeks," dan n=",n)
    # if (n != 0 and i != n):  
    if (indeks == n-1):
        # test
        print("sampai ke base")
        print("array di base")
        displayarraypoint(narray)
        # cari titik untuk panggil rekursi
        while (len(narray) != 1): # masih > 1 titik
            for i in range (0,len(narray)-1):
                temp = midpoint(narray[i],narray[i+1]) # midpoint antar indeks array
                points.append(temp) # list point
                narray[i] = temp # perbaiki nilai
            narray.pop() # keluarin terakhir (g dianggap lagi)
        print("hasil narray terakhir")
        displayarraypoint(narray)
        display.append(narray[0])
        points.append(narray[0])
        return narray[0] # nilai tengah akhir
    else: # sisanya hanya proses
        if (indeks == 1):
            print('haha salah')
        elif (indeks == 2):
            print('haha salah banget')
        elif (indeks == 0):
            print('haha apa yang terjadi')
        # untuk panggil rekursi dibagi 2, kiri dan kanan
        # print("awal banget")
        arraykiri = [narray[0]]
        arraykanan = [narray[len(narray)-1]]
        # print("setelah masukan awal")
        # displayarraypoint(arraykiri)
        # displayarraypoint(arraykanan)
        # displayarraypoint(arraykiri)
        # displayarraypoint(arraykanan)
        while (len(narray) != 1): # masih > 1 titik
            print("loop ke-",len(narray))
            for i in range (0,len(narray)-1): # loop untuk gabungin titik
                temp = midpoint(narray[i],narray[i+1])
                narray[i] = temp # perbaiki nilai
                points.append(temp) # list pointi
            narray.pop() # keluarin nilai terakhir (g dianggap lagi)
            print("setelah dihapus")
            displayarraypoint(narray)
            for j in range (len(narray)): # loop untuk test case
                print("yang dibandingkan")
                print(j," ",len(narray))
                if (len(narray) == 1): # tinggal satu -> dua-duanya
                    arraykiri.append(narray[j])
                    arraykanan.insert(0,narray[j])
                elif (len(narray) % 2 == 0): # perlakuan genap
                    if j < len(narray)/2: # 4 -> 0-1
                        arraykiri.append(narray[j])
                    elif j >= (len(narray)/2): # 4 -> 2-3
                        arraykanan.insert(0,narray[j])
                elif (len(narray) % 2 != 0): # perlakuan ganjil
                    if j < len(narray) // 2:  # 5 -> 0-1
                        arraykiri.append(narray[j])
                    elif j >= len(narray) / 2:  # 5 -> 3-4
                        arraykanan.insert(0, narray[j])
            # displayarraypoint(arraykanan)
            displayarraypoint(arraykiri)
            displayarraypoint(arraykanan)
            displayarraypoint(narray)
        print("iterasi ke-",indeks)
        displayarraypoint(arraykiri)
        displayarraypoint(arraykanan)
        displayarraypoint(narray)
        display.append(narray[0])
        # displayarraypoint(narray)
        # displayarraypoint(arraykiri)
        # displayarraypoint(arraykanan)

        # rekursi
        left_result = greedyqcgen(arraykiri, indeks + 1, n, points, display)
        right_result = greedyqcgen(arraykanan, indeks + 1, n, points, display)
        return midpoint(left_result, right_result)

# contoh penggunaan
titik1 = Point(1,1)
titik2 = Point(2,3)
titik3 = Point(3,1)
titik4 = Point(4,2)
temp = [titik1,titik2,titik3,titik4]

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

# if (jtitik == 2): # sisa 2 elemen
#     arraykiri.append(temp)
#     arraykanan.insert(0,temp)
# # elif (jtitik % 2 == 0 and i == (jtitik//2)-1): # di tengah genap
# #     arraykiri.append(midpoint(arraykiri[len(arraykiri)-1],temp))
# #     arraykanan.insert(0,midpoint(arraykanan[0],temp))
# # elif (jtitik % 2 != 0 and i == (jtitik//2)-1): # di tengah kiri ganjil
# #     arraykiri.append(midpoint(arraykiri[len(arraykiri)-1],temp))
# # elif (jtitik % 2 != 0 and i == (jtitik//2)+1): # di kanan tengah ganjil
# #     arraykanan.insert(0,midpoint(arraykanan[0],temp))
# elif (i < jtitik//2): # di kiri
#     arraykiri.append(temp)
# elif (i > jtitik//2+1): # di kanan
#     arraykanan.insert(0,temp)