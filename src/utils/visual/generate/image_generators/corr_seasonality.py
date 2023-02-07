from matplotlib import pyplot as plt
import numpy as np
import sys
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf


def corr_seasonality(color, dpi, image_path, extension):

    np.random.seed(42)

    samples = [np.sin(n/10) + np.random.normal(.1) for n in range(300)]


    fig, curr_ax = plt.subplots()
    sm.graphics.tsa.plot_acf(samples, lags=60, ax=curr_ax, color=color, vlines_kwargs={"colors": color})
    curr_ax.set_title("Autocorrelação de Série Com Sazonalidade")

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
