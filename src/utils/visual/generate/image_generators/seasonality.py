from matplotlib import pyplot as plt
import numpy as np


def seasonality(color, dpi, image_path, extension):

    np.random.seed(42)
    samples = [np.sin(n/10) + np.random.normal(.1) for n in range(300)]
    plt.plot(samples, label="Série", color=color)
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de série com sazonalidade")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
