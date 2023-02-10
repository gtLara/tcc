from matplotlib import pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
import pickle
import numpy as np


def get_moving_average(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def fit_loess_trend(series, frac=0.6, delta_frac=1e5, plot=False):

    dependent_var = np.arange(len(series))/10 # creates non datetime index for LOESS
    independent_var = series

    trend_fit = lowess(independent_var, dependent_var, frac=frac,
                       delta=len(independent_var)/delta_frac)

    index = trend_fit[:, 0]
    trend = trend_fit[:, 1]

    if plot:
        plt.plot(index, trend)
        plt.plot(index, series)
        plt.show()

    return trend


def loess(color, dpi, image_path, extension):

    with open("data/motor_current_samples.pkl", "rb") as file:
        data = pickle.load(file)

    samples = get_moving_average(data.values, 100)
    plt.plot(samples, color=color)

    trend_1 = fit_loess_trend(samples, frac=0.1)
    trend_3 = fit_loess_trend(samples)

    plt.plot(samples[:len(trend_1)], label="Série", color=color)
    plt.plot(trend_1, label="LOESS com 10% do sinal", color="black",
             linewidth=2, linestyle="--")

    plt.plot(trend_3, label="LOESS com 60% do sinal", color="red",
             linewidth=2, linestyle="--")

    plt.xlabel("Tempo[ms]")
    plt.ylabel("Amplitude [A/A]")
    plt.title("Exemplo de Aplicação de LOESS")
    plt.legend()

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
