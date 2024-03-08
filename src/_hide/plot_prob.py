import numpy as np
import matplotlib.pyplot as plt
import weighted_Sum

def p_list(p, interval_size, step_size):
    p_min = p - interval_size
    p_max = p + interval_size
    p_interval = np.arange(p_min, p_max, step_size, dtype=float)
    return p_interval

x_vals = p_list(0.5, 0.05, 0.01)
y_vals = weighted_Sum.p_iteration(0.5, 40, 0.05, 0.01)

plt.plot(x_vals, y_vals, marker='o')  # 'o' adds circle markers to each data point
plt.xlabel('p')  # Optional: Add label for the x-axis
plt.ylabel('Qp (Percolation Value)')  # Optional: Add label for the y-axis
plt.title('Simple Plot')   # Optional: Add title to the plot
plt.grid(True)              # Optional: Show grid
plt.show()