# 代码生成时间: 2025-09-15 11:34:52
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

"""
Interactive Chart Generator
This program allows the user to interactively create and modify charts using numpy data.
It includes features for dynamically adjusting parameters and real-time chart updates.
"""

# Define the function to generate the chart
def update(val):
    """Updates the chart with new parameters."""
    # Clear the current plot
    plt.clf()

    # Generate new data based on the sliders' values
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(amp_slider.val * x) + np.cos(frequency_slider.val * x)

    # Plot the new data
    plt.plot(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Interactive Chart')
    plt.ylim(-5, 5)

    # Redraw the canvas with the new plot
    plt.draw_idle()

# Define the main function to initialize the plot and sliders
def main():
    """Initializes the interactive chart with sliders."""
    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Create sliders for amplitude and frequency
    axcolor = 'lightgoldenrodyellow'
    ax_amp = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_freq = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)

    # Initialize the sliders' values
    initial_amp = 1.0
    initial_freq = 1.0

    # Create the amplitude slider
    amp_slider = Slider(ax_amp, 'Amplitude', 0.1, 5.0, valinit=initial_amp)
    amp_slider.on_changed(update)

    # Create the frequency slider
    frequency_slider = Slider(ax_freq, 'Frequency', 0.1, 10.0, valinit=initial_freq)
    frequency_slider.on_changed(update)

    # Call the update function initially to draw the chart
    update(0)

    # Show the plot with sliders
    plt.show()

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Call the main function to start the interactive chart generator
    main()