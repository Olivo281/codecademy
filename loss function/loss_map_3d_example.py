import matplotlib.pyplot as plt
import numpy as np

# Generate a range of x values
x = np.linspace(-3, 3, 400)

# Compute L1 and L2 values
l1 = np.abs(x)
l2 = x**2

# Plot both
plt.figure(figsize=(8, 5))
plt.plot(x, l1, label='L1: |x| (Manhattan)', color='blue')
plt.plot(x, l2, label='L2: x² (Euclidean)', color='red')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.title("L1 vs L2 Penalty")
plt.xlabel("Coefficient value (x)")
plt.ylabel("Penalty")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
