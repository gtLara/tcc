from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import acf
from matplotlib import pyplot as plt
import pickle
import numpy as np


def autocorrelation_peak_example(color, dpi, image_path, extension):

    with open("data/data_dict.pkl", "rb") as file:
        data = pickle.load(file)

    signal = data[1500]['[1017:4]'].iloc[:60*100*10]

    fig, ax = plt.subplots()
    plot_acf(signal, lags=15000, ax=ax, color=color,
             vlines_kwargs={"colors": color})

    first_peak = np.argmax(acf(signal, nlags=10000)[5000:7500]) + 5000
    plt.axvline(first_peak, color="red", linestyle="--", linewidth=2)
    plt.axvline(0, color="red", linestyle="--", linewidth=2)

    plt.xlabel("Atrasos")
    plt.ylabel("Correlação")
    plt.title("Visualização de Determinação de Período Sazonal a partir de " +
              "Autocorrelação")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
