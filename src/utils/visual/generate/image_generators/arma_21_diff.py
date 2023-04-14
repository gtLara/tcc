import numpy as np
import matplotlib.pyplot as plt
from src.utils.signals.generate.linear_models import generate_arma


def arma_21_diff(color, dpi, image_path, extension):

    ma_coef = [0.8, 1]
    ar_coef = [0.25, -0.5, 1]
    signal = np.diff(generate_arma(n_samples=250, ar_coef=ar_coef,
                                   ma_coef=ma_coef))

    plt.plot(signal, color=color)
    plt.title("Série Temporal de Processo ARMA(2, 1) Diferenciado")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
