import matplotlib.pyplot as plt

# Sample 2D coordinates
x_coordinates = [1, 3, 2, 4, 5]
y_coordinates = [2, 5, 3, 7, 11]

# Plotting the points without axes and grids
plt.scatter(x_coordinates, y_coordinates, label='Points', color='blue', marker='.')

# Remove x and y axes
plt.xticks([])  # Remove x-axis
plt.yticks([])  # Remove y-axis

# Adding legend
plt.legend()

# Display the plot
plt.show()
