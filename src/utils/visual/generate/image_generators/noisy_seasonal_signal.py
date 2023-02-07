import statsmodels.api as sm
from matplotlib import pyplot as plt
import numpy as np


def noisy_seasonal_signal(color, dpi, image_path, extension):

    np.random.seed(42)
    samples = [np.sin(n/10) + np.random.normal(scale=1.5) for n in range(300)]

    fig, ax = plt.subplots(2, 1)

    ax[0].plot(samples, label="Série", color=color)
    ax[0].set(xlabel="Tempo", ylabel="Magnitude",
              title="Série Imersa em Ruído")

    sm.graphics.tsa.plot_acf(samples, lags=150, ax=ax[1], color=color,
                             vlines_kwargs={"colors": color})
    ax[1].set(xlabel="Atrasos", ylabel="Correlação",
              title="Autocorrelação")

    fig.set_size_inches(8, 7)
    plt.tight_layout()
    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
