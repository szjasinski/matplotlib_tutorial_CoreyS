
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')

index = count()


def animate(self):
    data = pd.read_csv('data9.csv')

    # # last 60 seconds
    # x = data['x_value'][-60:]
    # y1 = data['total_1'][-60:]
    # y2 = data['total_2'][-60:]

    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()  # clear plots
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10)


plt.tight_layout()
plt.show()

