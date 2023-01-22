from matplotlib import pyplot as plt
import numpy as np

def random_walk(color, dpi, image_path, extension):
    y_0 = 5
    y = []
    y.append(y_0)

    for n in range(300):
        y.append(y[n-1]+np.random.normal(0, .1))

    plt.plot(y, color=color)
    plt.title("Caminhada Aleatória")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
