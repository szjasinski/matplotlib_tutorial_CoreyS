from matplotlib import pyplot as plt
import random

# plt.style.use('fivethirtyeight')

x_axis = [0]
y_axis = [0]

n = 0
count = 0
for x in range(1000000):
    l = random.randint(-1, 1)
    x_axis.append(x+1)
    y_axis.append(y_axis[count] + l)
    count += 1

plt.plot(x_axis, y_axis, label='random shit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('random chart')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()
