from matplotlib import pyplot as plt
from math import sqrt
import math
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation


def generate_x_axis(r, num):
    # r - radius, num - number of parts to which circle is divided
    angles = np.linspace(0, math.pi/2, num)
    x_axis_neg = [r*(1 - math.sin(angle)) for angle in angles]
    x_axis_neg.reverse()
    for id, val in enumerate(x_axis_neg):
        new_val = val - 3
        x_axis_neg[id] = new_val
    x_axis_pos = [-x for x in x_axis_neg]
    x_axis_pos.reverse()
    x_axis_pos.pop(0)
    # print(x_axis_pos)
    # print(x_axis_neg)
    return x_axis_neg + x_axis_pos


r = 3
num = 10
fragment_len = 8

x_axis_top = generate_x_axis(r, num)
y_axis_top = [sqrt(r ** 2 - x ** 2) for x in x_axis_top]

x_axis_bot = x_axis_top.copy()
x_axis_bot.reverse()
y_axis_bot = [-y for y in y_axis_top]
y_axis_bot.reverse()

print(x_axis_top)
print(x_axis_bot)


x_fragment_top = x_axis_top[:fragment_len]  # fist n items
y_fragment_top = y_axis_top[:fragment_len]
# x_fragment_bot = x_axis_bot[:fragment_len]
# y_fragment_bot = y_axis_bot[:fragment_len]
x_fragment_bot = []
y_fragment_bot = []


index = count(fragment_len)
DRAW_TOP_SIDE = False


def animate(i):
    global DRAW_TOP_SIDE
    n = next(index)
    axis_len = len(x_axis_top)

    # print("x_fragment_top", x_fragment_top)
    # print("y_fragment_top", y_fragment_top)
    # print("x_fragment_bot", x_fragment_bot)
    # print("y_fragment_bot", y_fragment_bot)
    # print("n", n)
    # print("axis_len", axis_len)
    # print("n % (2*axis_len)", n % (2*axis_len))
    # print("axis_len - fragment_len", axis_len - fragment_len)
    # print("n % axis_len", n % axis_len)
    # print("x_axis_top", x_axis_top)

    if n % (2*axis_len) < fragment_len:
        x_fragment_top.append(x_axis_top[n % axis_len])
        y_fragment_top.append(y_axis_top[n % axis_len])
        x_fragment_bot.pop(0)
        y_fragment_bot.pop(0)
    elif n % (2*axis_len) < axis_len:
        x_fragment_top.append(x_axis_top[n % axis_len])
        y_fragment_top.append(y_axis_top[n % axis_len])
        x_fragment_top.pop(0)
        y_fragment_top.pop(0)
    elif n % (2*axis_len) < axis_len + fragment_len:
        x_fragment_bot.append(x_axis_bot[n % axis_len])
        y_fragment_bot.append(y_axis_bot[n % axis_len])
        x_fragment_top.pop(0)
        y_fragment_top.pop(0)
    elif n % (2*axis_len) < 2*axis_len:
        x_fragment_bot.append(x_axis_bot[n % axis_len])
        y_fragment_bot.append(y_axis_bot[n % axis_len])
        x_fragment_bot.pop(0)
        y_fragment_bot.pop(0)

    print(n, "----------------------------")

    plt.cla()  # clear plots

    plt.plot(x_axis_top, y_axis_top, color='b', linewidth=3)
    plt.plot(x_axis_bot, y_axis_bot, color='b', linewidth=3)

    plt.plot(x_fragment_top, y_fragment_top, color='#00e526', linewidth=6)
    plt.plot(x_fragment_bot, y_fragment_bot, color='#00e526', linewidth=6)

    plt.grid(True)
    plt.gca().set_aspect("equal")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('circle')


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()

plt.show()
