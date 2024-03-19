import bruteforce
import dividenconquer
import dividenconquerumumbonus
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# inisialisasi kelas point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def displaypoint(t0):
    print(t0.x,t0.y)

def displayarraypoint(arr):
    for i in range (len(arr)):
        displaypoint(arr[i])
    print()

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
    display = bruteforce.spekqc(arraytitik[0],arraytitik[1],arraytitik[2],jiterasi)
    endbrute = time.time()
    executiontime = endbrute-startbrute
elif (jtitik == 3 and pilihan == 2): # divide and conquer
    startdnc = time.time()
    dividenconquer.dividenconquerqc(arraytitik[0],arraytitik[1],arraytitik[2],0,jiterasi,points,display)
    enddnc = time.time()
    executiontime = enddnc-startdnc
else: # divide and conquer bonus
    startdncbonus = time.time()
    dividenconquerumumbonus.dividenconquerqcgen(arraytitik,0,jiterasi,points,display)
    enddncbonus = time.time()
    executiontime = enddncbonus-startdncbonus

# Pisah point
xdisplay = [point.x for point in display]
ydisplay = [point.y for point in display]

# Urutkan untuk tampilan
sorted_indices = sorted(range(len(xdisplay)), key=lambda i: xdisplay[i])
x_values_sorted = [xdisplay[i] for i in sorted_indices]
y_values_sorted = [ydisplay[i] for i in sorted_indices]

# Plot the points
plt.plot(x_values_sorted, y_values_sorted, marker='o', linestyle='-')

plt.text(0.5, 1.05, f'Execution Time: {executiontime:.15f} seconds', transform=plt.gca().transAxes, fontsize=10)

# Display
plt.show()

# Buat sumbu
fig, ax = plt.subplots()

# animasi
def animate(frame):
    if frame < len(display):
        x_values = [point.x for point in display[:frame+1]]
        y_values = [point.y for point in display[:frame+1]]
        ax.clear()
        ax.plot(x_values, y_values, 'bo-')
        ax.set_xlim(min(x_values) - 1, max(x_values) + 1)
        ax.set_ylim(min(y_values) - 1, max(y_values) + 1)

ani = animation.FuncAnimation(fig, animate, frames=len(display), interval=300, blit=False)
plt.show()

