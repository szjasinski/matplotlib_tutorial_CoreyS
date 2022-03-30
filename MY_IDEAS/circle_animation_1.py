from matplotlib import pyplot as plt
from math import sqrt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation

r = 3
x_axis = np.linspace(-r, r, 20)
y_axis_plus = [sqrt(r**2-x**2) for x in x_axis]
y_axis_minus = [-y for y in y_axis_plus]


x_vals = [x_axis[0]]
y_vals_plus = [y_axis_plus[0]]
y_vals_minus = [y_axis_plus[0]]

index = count()


def animate(i):
    n = next(index)
    if n < len(x_axis):
        x_vals.append(x_axis[n])
        y_vals_plus.append(y_axis_plus[n])
        y_vals_minus.append(y_axis_minus[n])

        plt.cla()  # clear plots
        plt.plot(x_vals, y_vals_plus, color='b')
        plt.plot(x_vals, y_vals_minus, color='b')

        plt.grid(True)
        plt.gca().set_aspect("equal")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('circle')


ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()

plt.show()
