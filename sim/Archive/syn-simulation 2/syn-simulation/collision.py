import numpy as np
import matplotlib.pyplot as plt
# Define the function you want to plot
def my_function(x):
    return (1 - 1 / x) ** (x-1)
# Generate x values
x = np.linspace(2, 100, 99)
# Calculate y values by applying the function to x
y = my_function(x)
# Create the plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.plot(x, y, color='blue')  # Replace 'y = x^2' with a label for your function
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot of a Function')
plt.grid(True)
plt.legend()
# Show the plot
plt.show()



