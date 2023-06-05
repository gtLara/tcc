from src.utils.signals.anomaly_detection import detect_by_linear_inclination
import numpy as np
from matplotlib import pyplot as plt
import pickle


def anomaly_detection(color, dpi, image_path, extension):

    with open("data/anomalous_residuals.pkl", "rb") as file:
        data = pickle.load(file)

    shutdown_indices = slice(177500, 196000)
    shutdown_mask = np.zeros(len(data), dtype=bool)
    shutdown_mask[shutdown_indices] = True

    anomaly_indices = detect_by_linear_inclination(data, shutdown_mask)

    plt.plot(data.values, color=color,
             label="Acusação de Regime de Normalidade")
    plt.plot(np.where(anomaly_indices)[0], data[anomaly_indices].values,
             label="Acusação de Regime de Anomalia",
             color="r", linewidth=2)

    plt.axvline(295000, color="k", label="Momento registrado de anomalia")
    plt.legend()

    plt.xlabel("Tempo[ms]")
    plt.ylabel("Amplitude [A/A]")
    plt.title("Visualização de Detecção de Anomalia")
    plt.legend()

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
