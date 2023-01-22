from matplotlib import pyplot as plt
import numpy as np

def trend(color, dpi, image_path, extension):
    np.random.seed(42)
    samples = [np.random.normal(n/30) for n in range(200)]
    trend = [n/30 for n in range(200)]

    plt.plot(samples, label="Série", color=color)
    plt.plot(trend, label="Tendência", color="black", linewidth=1, linestyle="--")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de série com tendência")
    plt.legend()

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
