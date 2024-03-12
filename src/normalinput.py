# Initialize empty lists to store x and y coordinates
x_coordinates = []
y_coordinates = []

print("Masukkan data berikut:")
for i in range(3):
    xtemp = input("x ke-{}: ".format(i+1))
    ytemp = input("y ke-{}: ".format(i+1))
    x_coordinates.append(float(xtemp))
    y_coordinates.append(float(ytemp))

print(x_coordinates)
print(y_coordinates)
