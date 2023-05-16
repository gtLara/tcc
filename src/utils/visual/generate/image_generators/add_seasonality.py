from matplotlib import pyplot as plt
import numpy as np


def add_seasonality(color, dpi, image_path, extension):

    samples = [5*np.sin(n/10) + np.random.normal(n/10, 2.5) for n in range(400)]
    trend = [n/10 for n in range(400)]

    plt.plot(samples, label="Série", color=color)
    plt.plot(trend, label="Tendência", color="black", linewidth=1, linestyle="--")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de série com sazonalidade aditiva")
    plt.legend()

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
