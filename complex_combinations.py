import matplotlib.pyplot as plt
import numpy as np

# Initial positions of p0 and p1
p0 = 1 + 0j
p1 = 1j

# Maximum value of the axis (change this value as needed)
max_axis_value = 5

# Create a figure and axis
fig, ax = plt.subplots()


# Function to update the plot
def update_plot():
    ax.clear()  # Clear the previous plot
    ax.set_aspect("equal")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)

    # Plot p0 in red and p1 in blue
    pair = np.array([p0, p1])
    ax.plot(pair.real, pair.imag, "ko", label=r"$p_0, p_1$")

    mean = (p0 + p1) / 2
    ax.plot(mean.real, mean.imag, "co", label=r"$(p_0 + p_1) / 2$")

    geometric_mean = np.sqrt(p0 * p1) * np.array([1, -1])
    ax.plot(geometric_mean.real, geometric_mean.imag, "mo", label=r"$\sqrt{p_0  p_1}$")

    quadrature = np.sqrt(p0**2 + p1**2) * np.array([1, -1])
    ax.plot(quadrature.real, quadrature.imag, "yo", label=r"$\sqrt{p_0^2 +  p_1^2}$")

    # Set the axis limits
    ax.set_xlim(-max_axis_value, max_axis_value)
    ax.set_ylim(-max_axis_value, max_axis_value)

    # Display labels for axes
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")

    # Display legend
    ax.legend()

    # Refresh the plot
    fig.canvas.draw()


# Function to handle mouse clicks
def on_click(event):
    global p0, p1
    if event.button == 1:  # Left click
        p0 = complex(event.xdata, event.ydata)
    elif event.button == 3:  # Right click
        p1 = complex(event.xdata, event.ydata)
    update_plot()


# Create the initial plot
update_plot()

# Connect the mouse click event handler
fig.canvas.mpl_connect("button_press_event", on_click)

# Show the plot
plt.show()
