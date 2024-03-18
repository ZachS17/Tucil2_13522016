import bruteforce
import dividenconquer
import dividenconquerumumbonus
import matplotlib.pyplot as plt
import time

# inisialisasi kelas point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

while True:
    try:
        # Minta input
        jtitik = int(input("Masukkan banyak titik: "))
        
        # Cek brute force atau divide and conquer (tidak ada brute force untuk bonus)
        if jtitik != 3 and jtitik > 0:
            pilihan = 2
            break
        elif jtitik == 3:
            break
        else:
            print("Masukkan bilangan positif\n")
    except ValueError:
        # bukan integer
        print("Masukkan angka yang benar\n")

# fungsi validasi titik
def get_point_input(indeks):
    while True:
        try:
            titikmasukan = input("Titik ke-"+ str(indeks) + ": ")
            
            # Pisah
            xstr, ystr = titikmasukan.split(',')
            
            # Ubah jadi float
            x = float(xstr)
            y = float(ystr)
            
            # Mengeluarkan titiknya
            return Point(x, y)
        except ValueError:
            # Coba sampai valid
            print("Masukkan lagi sesuai format <x,y>\n")

# minta masukan titik
arraytitik = []
print("Masukkan titik sesuai format <x,y>")
for i in range (jtitik):
    temp = get_point_input(i+1)
    arraytitik.append(temp)
print()

# minta jumlah iterasi
while True:
    try:
        # Minta input
        jiterasi = int(input("Masukkan jumlah iterasi: "))
        
        # Cek brute force atau divide and conquer (tidak ada brute force untuk bonus)
        if jiterasi <= 0:
            print("Masukkan angka positif\n")
        else:
            break
    except ValueError:
        # bukan integer
        print("Masukkan angka yang benar\n")

# sesuai masukan
if (jtitik == 3):
    while True:
        try:
            # Ask for input
            print("Pilih algoritma penyelesaian:")
            print("1. Brute Force")
            print("2. Divide and Conquer")
            pilihan = int(input("Masukkan pilihan: "))
            
            # Cek brute force atau divide and conquer
            if pilihan < 1 or pilihan > 2: # salah input
                print("Masukkan angka yang benar (1 atau 2)\n")
            else: # bisa kedua cara
                break
        except ValueError:
            # bukan integer
            print("Masukkan angka yang benar (1 atau 2)\n")

# inisialisasi array untuk diisi
points = []
display = []

# operasi
if (jtitik == 3 and pilihan == 1): # brute force
    startbrute = time.time()
    points, display = bruteforce.brutemidqc(arraytitik[0],arraytitik[1],arraytitik[2],jiterasi)
    endbrute = time.time()
    print("Waktu eksekusi: ",endbrute-startbrute,"detik")
elif (jtitik == 3 and pilihan == 2): # divide and conquer
    startdnc = time.time()
    dividenconquer.greedyqc(arraytitik[0],arraytitik[1],arraytitik[2],0,jiterasi,points,display)
    enddnc = time.time()
    print("Waktu eksekusi: ",enddnc-startdnc,"detik")
else: # divide and conquer bonus
    startdncbonus = time.time()
    dividenconquerumumbonus.greedyqcgen(arraytitik,0,jiterasi,points,display)
    enddncbonus = time.time()
    print("Waktu eksekusi:",enddncbonus-startdncbonus,"detik")

# Pisah point
xdisplay = [point.x for point in display]
ydisplay = [point.y for point in display]

# Plot
plt.scatter(xdisplay, ydisplay, label='Points', color='blue', marker='.')

# Display
plt.show()

