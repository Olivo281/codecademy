# Part 1: Define functions for line and error calculation

def get_y(m, b, x):
    """
    Calculate y = m*x + b for given m, b, and x.
    """
    return m * x + b

# Uncomment to test get_y:
# print(get_y(2, 1, 3))  # Expected 7
# print(get_y(0, 0, 5))  # Expected 0

def calculate_error(m, b, point):
    """
    Calculate the vertical distance between a point and the line y = m*x + b.
    point is a tuple or list: (x, y)
    """
    x_point = point[0]
    y_point = point[1]
    y_on_line = get_y(m, b, x_point)
    error = abs(y_on_line - y_point)
    return error

# Uncomment to test calculate_error:
# print(calculate_error(1, 0, (3, 3)))  # Expected 0
# print(calculate_error(1, 0, (3, 4)))  # Expected 1
# print(calculate_error(0, 0, (0, 1)))  # Expected 1

def calculate_all_error(m, b, points):
    """
    Calculate the total error between a set of points and the line y = m*x + b.
    """
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

# Example datapoints for testing
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# Uncomment to test calculate_all_error:
# print(calculate_all_error(1, 0, datapoints))  # Check value
# print(calculate_all_error(0, 1, datapoints))  # Check value

# Part 2: Try a bunch of slopes (m) and intercepts (b) to minimize error

possible_ms = [m / 10 for m in range(-100, 101)]  # from -10 to 10 inclusive, step 0.1
possible_bs = [b / 10 for b in range(-200, 201)]  # from -20 to 20 inclusive, step 0.1

smallest_error = float('inf')
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b

print(f"Best m: {best_m}")
print(f"Best b: {best_b}")
print(f"Smallest error: {smallest_error}")

# Part 3: Use best line to predict bounce height for width=6

predicted_y = get_y(best_m, best_b, 6)
print(f"Predicted bounce height for ball with width 6: {predicted_y}")
