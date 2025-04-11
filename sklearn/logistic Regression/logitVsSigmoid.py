import numpy as np
import matplotlib.pyplot as plt
from scipy.special import logit, expit  # logit = inverse sigmoid, expit = sigmoid

# Define probability range for logit function
p_values = np.linspace(0.01, 0.99, 100)  # Avoiding 0 and 1 to prevent log issues
logit_values = logit(p_values)  # Apply logit function

# Define x range for sigmoid function
x_values = np.linspace(-6, 6, 100)
sigmoid_values = expit(x_values)  # Apply sigmoid function

# Plot Logit Function
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(p_values, logit_values, label="Logit Function", color="red")
plt.xlabel("Probability (p)")
plt.ylabel("Log-Odds (logit)")
plt.title("Logit Function: Probability to Log-Odds")
plt.grid()
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axvline(0.5, color='black', linestyle='--', linewidth=0.5)
plt.legend()

# Plot Sigmoid Function
plt.subplot(1, 2, 2)
plt.plot(x_values, sigmoid_values, label="Sigmoid Function", color="blue")
plt.xlabel("Log-Odds (x)")
plt.ylabel("Probability (p)")
plt.title("Sigmoid Function: Log-Odds to Probability")
plt.grid()
plt.axhline(0.5, color='black', linestyle='--', linewidth=0.5)
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.show()
