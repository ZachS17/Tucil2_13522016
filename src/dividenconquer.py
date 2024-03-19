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

# points, display declare dari luar fungsi kosong dan akan diisi 
def dividenconquerqc(t0,t1,t2,i,n,points,display):
    if (i == n-1):
        # hitung dan masukin array
        newt1kiri = midpoint(t0,t1)
        points.append(newt1kiri)
        newt1kanan = midpoint(t1,t2)
        points.append(newt1kanan)
        newcomb = midpoint(newt1kiri,newt1kanan)
        points.append(newcomb)
        display.append(newcomb)
        return newcomb
    
    else: # sisanya dipisah
        # hitung dan masukin array
        newt1kiri = midpoint(t0,t1)
        points.append(newt1kiri)
        newt1kanan = midpoint(t1,t2)
        points.append(newt1kanan)
        newcomb = midpoint(newt1kiri,newt1kanan)
        points.append(newcomb)

        # masukin display
        display.append(newcomb)

        # rekursi
        left_result = dividenconquerqc(t0, newt1kiri, newcomb, i + 1, n, points, display)
        right_result = dividenconquerqc(newcomb, newt1kanan, t2, i + 1, n, points, display)
        return midpoint(left_result, right_result)