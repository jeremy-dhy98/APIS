import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Set major ticks
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(-1, 1.5, 0.5))

# Set minor ticks
ax.set_xticks(np.arange(0, 10.1, 0.2), minor=True)
ax.set_yticks(np.arange(-1, 1.1, 0.1), minor=True)

# Customize tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Show the plot
plt.show()
