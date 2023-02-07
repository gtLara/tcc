from matplotlib import pyplot as plt
import numpy as np


def difference_example(color, dpi, image_path, extension):
    np.random.seed(42)
    samples = [np.random.normal(n/30) for n in range(100)]

    plt.plot(samples, label="y", color=color)
    plt.plot(np.diff(samples, 1), color="black", linestyle="--", label=r"$\nabla$y", linewidth=0.9)
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de uso de operador de diferenças")
    plt.legend()

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
