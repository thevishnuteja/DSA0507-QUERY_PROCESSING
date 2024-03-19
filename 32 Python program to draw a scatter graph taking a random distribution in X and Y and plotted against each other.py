import matplotlib.pyplot as plt
import numpy as np
num_points = 100
x = np.random.rand(num_points)
y = np.random.randn(num_points)
plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Random Distributions")
plt.show()
