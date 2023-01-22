from matplotlib import pyplot as plt
import numpy as np

def log_trend(color, dpi, image_path, extension):
    np.random.seed(42)
    samples = [np.random.normal(np.log(n/10), 0.6) for n in range(400)]
    trend = [np.log(n/10) for n in range(400)]

    plt.plot(samples, label="Série", color=color)
    plt.plot(trend, label="Tendência", color="black", linewidth=1, linestyle="--")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de série com tendência logarítmica")
    plt.legend()

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
