import time as time

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

def dividenconquerqcgen(narray,indeks,n,points,display): # points,display declare dari luar fungsi kosong dan akan diisi
    if (indeks == n-1):
        while (len(narray) != 1): # masih > 1 titik
            for i in range (0,len(narray)-1):
                temp = midpoint(narray[i],narray[i+1]) # midpoint antar indeks array
                points.append(temp) # list point
                narray[i] = temp # perbaiki nilai
            narray.pop() # keluarin terakhir (g dianggap lagi)

        # masukan display dan point
        display.append(narray[0])
        points.append(narray[0])

        return narray[0] # nilai tengah akhir
    
    else: # sisanya dipisah
        arraykiri = [narray[0]]
        arraykanan = [narray[-1]]
        while (len(narray) != 1): # masih > 1 titik
            for i in range (0,len(narray)-1): # loop untuk gabungin titik
                temp = midpoint(narray[i],narray[i+1])
                narray[i] = temp # perbaiki nilai
                points.append(temp) # list pointi
            narray.pop() # keluarin nilai terakhir (g dianggap lagi)
            for j in range (len(narray)): # loop untuk test case
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

        # masukin display
        display.append(narray[0])

        # rekursi
        left_result = dividenconquerqcgen(arraykiri, indeks + 1, n, points, display)
        right_result = dividenconquerqcgen(arraykanan, indeks + 1, n, points, display)
        return midpoint(left_result, right_result)