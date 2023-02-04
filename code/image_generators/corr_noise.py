from matplotlib import pyplot as plt
import numpy as np
import sys
import statsmodels.api as sm
from matplotlib.collections import PolyCollection


def corr_noise(color, dpi, image_path, extension):

    np.random.seed(42)
    samples = [np.random.normal() for n in range(200)]

    fig, curr_ax = plt.subplots()
    sm.graphics.tsa.plot_acf(samples, lags=15, ax=curr_ax, color=color,
                             vlines_kwargs={"colors": color})
    curr_ax.set_title("Autocorrelação de Ruído Branco")

    for item in curr_ax.collections:
        if type(item) == PolyCollection:
            item.set_facecolor("red")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
