from matplotlib import pyplot as plt
import numpy as np

# Exemplo de serie no tempo

def white_noise(color, dpi, image_path, extension):

    np.random.seed(42)
    samples = [np.random.normal() for n in range(200)]

    plt.plot(samples, color=color)
    plt.title("Exemplo de Série no Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
