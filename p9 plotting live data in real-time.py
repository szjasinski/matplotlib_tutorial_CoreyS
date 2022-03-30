
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')

x_vals = [0]
y_vals = [0]

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(y_vals[-1]+random.randint(-1, 1))

    plt.cla()  # clear plots
    plt.plot(x_vals, y_vals, linewidth=2)


ani = FuncAnimation(plt.gcf(), animate, interval=10)


plt.tight_layout()
plt.show()
