from matplotlib import pyplot as plt
import numpy as np

def get_moving_average(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def moving_average(color, dpi, image_path, extension):
    np.random.seed(42)
    samples = [np.random.normal(n/30) for n in range(200)]
    m = 15

    trend = get_moving_average(samples, m)

    plt.plot(samples[:len(trend)], label="Série", color=color)
    plt.plot(trend, label=f"Média Móvel de Ordem {m}", color="black", linewidth=2, linestyle="--")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")
    plt.title("Exemplo de Aplicação de Média Móvel")
    plt.legend()

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()

