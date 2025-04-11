# Function to compute y = mx + b
def get_y(m, b, x):
    return m * x + b

# Function to compute the error between a point and the line
def calculate_error(m, b, point):
    x_point, y_point = point
    y = get_y(m, b, x_point)
    distance = abs(y - y_point)
    return distance

# Function to compute the total error for a line given multiple points
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

# Dataset of points
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# Generate possible slopes (m) and intercepts (b)
possible_ms = [i * 0.1 for i in range(-100, 101)]  # -10 to 10 inclusive
possible_bs = [i * 0.1 for i in range(-200, 201)]  # -20 to 20 inclusive

# Variables to store the best values
smallest_error = float("inf")
best_m = 0
best_b = 0

# Find the line of best fit
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b

# Print the best values
print("Best m:", best_m)
print("Best b:", best_b)
print("Smallest error:", smallest_error)

# Use the best line to predict the bounce height for x = 6
x_value = 6
predicted_y = get_y(best_m, best_b, x_value)
print(f"The predicted bounce height for a 6cm ball is: {predicted_y}")
