from pathlib import Path
# import numpy as np
import pickle
import matplotlib.pyplot as plt
# import pandas as pd
# from utils.features.decomposition import fit_loess_trend, model_seasonal_component, decompose
# from utils.visual.acf import plot_acf
# from utils.visual.decomposition import plot_decomposition
plt.style.use("ggplot")

dplot = True

# Sucata às 14:49 na gaiola 17


def current_signal_demos(color, dpi, image_path, extension):

    path = Path("./data")

    with open(path/"data_dict.pkl", "rb") as file:
        data = pickle.load(file)

    currents = data[1500][:100*60*3]  # for 16 currents
    currents = currents.drop(currents.columns[:11], axis=1)

    series_figure, series_axes = plt.subplots(3, 3)

    for i, (current, current_data) in enumerate(currents.iteritems()):

        filtered_current_data = current_data.rolling(window=100).mean().dropna()

        col = i % 3
        row = int(i/3)

        series_axes[row][col].plot(filtered_current_data, color=color,
                                   linewidth=0.7)

        series_axes[row][col].set_title(f"{i+1}")
        series_axes[row][col].set_xticks([])
        # series_axes[row][col].axvline(filtered_current_data.index[295000])

    series_figure.suptitle("Visualizações de Exemplos de Correntes", size=17)
    series_figure.tight_layout()
    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
