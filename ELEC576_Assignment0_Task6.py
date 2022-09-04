# Hsuan-You(Shaun) Lin / S01435165
# ELEC 576 - Fall 2022
# Assignment 0
#Task 6

import numpy as np
import matplotlib.pyplot as plt

# x values of the sine wave
time = np.arange(0, 10, 0.1);

amplitude = np.sin(time)

# Plot a sine wave
plt.plot(time, amplitude)

# Set title, x-axis/y-axis label, gird...etc for the sine wave plot
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude = sin(time)')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

# Display the sine wave
plt.show()