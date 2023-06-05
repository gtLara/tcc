from matplotlib import pyplot as plt
from pykalman import KalmanFilter
import pickle
import numpy as np
from src.utils.models.trend import get_kalman_trend


def kalman_trend(color, dpi, image_path, extension):

    with open("data/motor_current_samples.pkl", "rb") as file:
        data = pickle.load(file)

    samples = data.rolling(window=60).mean().dropna()

    trend = get_kalman_trend(samples, initial_mean=np.mean(samples),
                             transition_variance=.5e-7)

    plt.plot(samples.values, color=color, label="Sinal")
    plt.plot(trend, color="red", linestyle="--", label="Tendência Estrutural")

    plt.xlabel("Tempo[ms]")
    plt.ylabel("Amplitude [A/A]")
    plt.title("Exemplo de Modelagem Estrutural de Tendência")
    plt.legend()

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
