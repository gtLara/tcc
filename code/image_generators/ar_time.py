import matplotlib.pyplot as plt
import numpy as np

def ar_time(color, dpi, image_path, extension):
    y = np.zeros(300)

    plt.subplot(2, 2, 1)

    for n in range(300):
        y[n] = 0.28*y[n-1] + np.random.random()

    plt.plot(y, color=color)
    plt.title("a) AR(1)")
    plt.subplot(2, 2, 2)

    for n in range(300):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + np.random.random()

    plt.plot(y, color=color)
    plt.title("b) AR(2)")
    plt.subplot(2, 2, 3)

    for n in range(300):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + 0.39*y[n-3] + np.random.random()

    plt.plot(y, color=color)
    plt.title("c) AR(3)")
    plt.subplot(2, 2, 4)

    for n in range(300):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + 0.09*y[n-3] + 0.21*y[n-4] + np.random.random()

    plt.plot(y, color=color)
    plt.title("d) AR(4)")

    path=f"{image_path}.{extension}"
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, format=extension)
