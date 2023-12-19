import numpy as np

# Given data
x_values = np.array([0.05, 0.07, 0.08, 0.09, 0.11])
y_values = np.array([0.0404, 0.0398, 0.0393, 0.0387, 0.0381])

# Calculate the mean
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Calculate the slope (a)
numerator = np.sum((x_values - mean_x) * (y_values - mean_y))
denominator = np.sum((x_values - mean_x)**2)
slope_a = numerator / denominator

# Calculate the intercept (b)
intercept_b = mean_y - slope_a * mean_x

print(slope_a, intercept_b)