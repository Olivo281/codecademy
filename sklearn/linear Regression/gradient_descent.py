import matplotlib.pyplot as plt

# Function to compute gradient for intercept (b)
def get_gradient_at_b(x, y, b, m):
    """
    Computes the gradient for the intercept (b) in linear regression.
    
    Parameters:
    x (list): Input feature values
    y (list): Target values
    b (float): Current intercept
    m (float): Current slope

    Returns:
    float: The gradient of the cost function with respect to b
    """
    N = len(x)  # Number of data points
    diff = 0  # Initialize sum of differences
    
    # Compute the difference between actual and predicted values
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    
    # Compute the gradient (partial derivative of cost function w.r.t. b)
    b_gradient = -(2/N) * diff  
    return b_gradient

# Function to compute gradient for slope (m)
def get_gradient_at_m(x, y, b, m):
    """
    Computes the gradient for the slope (m) in linear regression.

    Parameters:
    x (list): Input feature values
    y (list): Target values
    b (float): Current intercept
    m (float): Current slope

    Returns:
    float: The gradient of the cost function with respect to m
    """
    N = len(x)  # Number of data points
    diff = 0  # Initialize sum of differences
    
    # Compute the weighted difference between actual and predicted values
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    
    # Compute the gradient (partial derivative of cost function w.r.t. m)
    m_gradient = -(2/N) * diff  
    return m_gradient

# Function to perform one step of gradient descent
def step_gradient(b_current, m_current, x, y, learning_rate):
    """
    Performs one step of gradient descent to update b and m.

    Parameters:
    b_current (float): Current intercept
    m_current (float): Current slope
    x (list): Input feature values
    y (list): Target values
    learning_rate (float): Step size for gradient descent

    Returns:
    list: Updated values of b and m
    """
    # Compute gradients for b and m
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
# The problem is that the distance formula treats all dimensions equally, regardless of their scale. If two movies came out 70 years apart, that should be a pretty big deal. However, right now, that’s exactly equivalent to two movies that have a difference in budget of 70 dollars. The difference in one year is exactly equal to the difference in one dollar of budget. That’s absurd!
    # Update parameters using gradient descent formula
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    
    return [b, m]  # Return updated parameters

# Function to perform full gradient descent optimization
def gradient_descent(x, y, learning_rate, num_iterations):
    """
    Runs gradient descent for a given number of iterations to optimize b and m.

    Parameters:
    x (list): Input feature values
    y (list): Target values
    learning_rate (float): Step size for gradient descent
    num_iterations (int): Number of iterations to run gradient descent

    Returns:
    list: Final optimized values of b and m
    """
    b = 0  # Initial intercept
    m = 0  # Initial slope
    
    # Perform multiple iterations of gradient descent
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)

    return [b, m]  # Return final optimized values

# Sample dataset: Months vs Revenue
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# Running gradient descent with a learning rate of 0.01 for 1000 iterations
b, m = gradient_descent(months, revenue, 0.01, 1000)

# Generate predicted values using the optimized line equation y = mx + b
y = [m*x + b for x in months]

# Plot original data points
plt.plot(months, revenue, "o", label="Actual Data")

# Plot the regression line
plt.plot(months, y, label="Best Fit Line", color='red')

plt.xlabel("Months")
plt.ylabel("Revenue")
plt.legend()
plt.title("Linear Regression using Gradient Descent")
plt.show()
