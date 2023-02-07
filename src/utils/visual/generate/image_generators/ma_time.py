import matplotlib.pyplot as plt
import numpy as np


def ma_time(color, dpi, image_path, extension):
    y = np.zeros(300)

    plt.subplot(2, 2, 1)

    for n in range(300):
        y[n] = 0.28*y[n-1] + np.random.random()

    plt.plot(y, color=color)
    plt.title("a) MA(1)")
    plt.subplot(2, 2, 2)

    for n in range(300):
        y[n] = 0.28*np.random.random() + 0.15*np.random.random() + \
               np.random.random()

    plt.plot(y, color=color)
    plt.title("b) MA(2)")
    plt.subplot(2, 2, 3)

    for n in range(300):
        y[n] = 0.28*np.random.random() + 0.15*np.random.random() + \
               0.39*np.random.random() + np.random.random()

    plt.plot(y, color=color)
    plt.title("c) MA(3)")
    plt.subplot(2, 2, 4)

    for n in range(300):
        y[n] = 0.28*np.random.random() + 0.15*np.random.random() + \
               0.09*np.random.random() + 0.21*np.random.random() + np.random.random()

    plt.plot(y, color=color)
    plt.title("d) MA(4)")

    path = f"{image_path}.{extension}"
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
