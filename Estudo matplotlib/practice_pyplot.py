# https://matplotlib.org/3.1.1/gallery/color/named_colors.html
import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4], 'ro')
# plt.show()

x = np.arange(0, 10, 0.1)
fig1, f1_axes = plt.subplots(ncols = 2, nrows = 2)

f1_axes[0, 0].plot(np.sin(x))
f1_axes[0, 0].plot(np.cos(x))
f1_axes[0, 0].set_title("Caixa 1")
f1_axes[0, 0].set_xlabel("Caixa 1 - Label X")
f1_axes[0, 0].set_ylabel("Caixa 1 - Label Y")

f1_axes[0, 1].plot(np.cos(x))
f1_axes[0, 1].set_title("Caixa 2")
f1_axes[0, 1].set_xlabel("Caixa 2 - Label X")
f1_axes[0, 1].set_ylabel("Caixa 2 - Label Y")

f1_axes[1, 0].plot(np.tan(x))
f1_axes[1, 0].set_title("Caixa 3")
f1_axes[1, 0].set_xlabel("Caixa 3 - Label X")
f1_axes[1, 0].set_ylabel("Caixa 3 - Label Y")

