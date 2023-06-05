from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
from matplotlib import pyplot as plt
import pickle


def anomalous_residuals(color, dpi, image_path, extension):

    with open("data/anomalous_residuals.pkl", "rb") as file:
        data = pickle.load(file)

    figure, axes = plt.subplots(2, 1)
    axes[0].plot(data, color=color)

    axes[0].set_xlabel("Tempo[ms]")
    axes[0].set_ylabel("Amplitude [A/A]")
    axes[0].set_title("Visualização de resíduos em regime de anomalia")

    plot_acf(data, lags=15000, ax=axes[1], color=color,
             vlines_kwargs={"colors": color})

    axes[1].set_xlabel("Atrasos")
    axes[1].set_ylabel("Autocorrelação")
    axes[1].set_title("Visualização autocorrelação de resíduos em regime de " +
                      "anomalia")

    figure.tight_layout()

    path = f"{image_path}.{extension}"
    figure.savefig(path, dpi=dpi, format=extension)
    plt.close()
