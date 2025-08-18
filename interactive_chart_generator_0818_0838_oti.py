# 代码生成时间: 2025-08-18 08:38:42
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from ipywidgets import interact

"""
Interactive Chart Generator
A Python script to generate interactive charts using matplotlib and ipywidgets.
Users can adjust parameters to modify the chart in real-time.
"""

class InteractiveChartGenerator:
    def __init__(self):
        # Initialize the figure and axis for plotting
        self.fig, self.ax = plt.subplots()

    def plot_function(self, x, amplitude=1, frequency=1):
        """
        Plot a sine wave function on the current axis with given parameters.

        Parameters:
        x (np.ndarray): Array of x values
        amplitude (float): Amplitude of the sine wave
        frequency (float): Frequency of the sine wave
        """
        # Calculate y values based on the sine function
        y = amplitude * np.sin(2 * np.pi * frequency * x)
        # Clear the current axis and plot the new function
        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Interactive Sine Wave Chart')
        plt.draw()

    def interactive_plot(self):
        """
        Generate an interactive plot with sliders for parameters adjustment.
        """
        # Define the range for the x values
        x = np.linspace(0, 2 * np.pi, 400)
        # Use ipywidgets to create sliders for amplitude and frequency
        interact(self.plot_function, x=x, amplitude=(0.1, 5.0), frequency=(0.1, 5.0))

# Create an instance of the InteractiveChartGenerator
chart_generator = InteractiveChartGenerator()

# Run the interactive plot function
chart_generator.interactive_plot()
