from matplotlib import pyplot as plt
from math import sqrt
import numpy as np

# x_axis = [x for x in range(100)]
# y_axis = [y**2 for y in x_axis]

r = 3

x_axis = np.linspace(-r, r, 200)
y_axis_plus = [sqrt(r**2-x**2) for x in x_axis]
y_axis_minus = [-y for y in y_axis_plus]


plt.plot(x_axis, y_axis_plus, color='b')
plt.plot(x_axis, y_axis_minus, color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('circle')

plt.grid(True)
plt.gca().set_aspect("equal")

plt.tight_layout()

plt.show()
