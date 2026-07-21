import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(x):
    var = 1 / (1 + np.exp(-x))
    return var

# Generate input values from -10 to 10
x = np.linspace(-10, 10, 100)

# Compute sigmoid values
y = sigmoid(x)

# Plot the sigmoid curve
plt.plot(x, y, label="Sigmoid Function")

# Add labels and title
plt.title("Sigmoid Function")
plt.xlabel("Input (x)")
plt.ylabel("Sigmoid(x)")

# Add grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.show()