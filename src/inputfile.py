import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the file
file_path = os.path.join(script_dir, "..", "test", "test1.txt")

# Initialize empty lists to store x and y coordinates
x_coordinates = []
y_coordinates = []

# Open the file and read the coordinates
with open(file_path, "r") as file:
    for line in file:
        # Split each line into x and y coordinates
        x_str, y_str = line.strip().split(',')
        
        # Convert strings to floats and add to the respective lists
        x_coordinates.append(float(x_str))
        y_coordinates.append(float(y_str))

# Print the extracted coordinates
print("X Coordinates:", x_coordinates)
print("Y Coordinates:", y_coordinates)
