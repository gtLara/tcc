import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


def ma_corr(color, dpi, image_path, extension):

    np.random.seed(42)
    size = 500
    lag = 9

    y = np.zeros(size)
    r = np.random.random(size)

    fig, axis = plt.subplots(2, 2)

    for n in range(size):
        y[n] = 0.28*r[n] + 0.15*r[n-1]

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[0][0], color=color,
                             vlines_kwargs={"colors": color})

    axis[0][0].set_title("a) MA(1)")

    for n in range(size):
        y[n] = 0.28*r[n] + 0.15*r[n-1] + 0.39*r[n-2]

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[0][1], color=color,
                             vlines_kwargs={"colors": color})

    axis[0][1].set_title("a) MA(2)")

    for n in range(size):
        y[n] = 0.28*r[n] + 0.15*r[n-1] + 0.39*r[n-2] + 0.12*r[n-3]

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[1][0], color=color,
                             vlines_kwargs={"colors": color})

    axis[1][0].set_title("a) MA(3)")

    for n in range(size):
        y[n] = 0.28*r[n] + 0.15*r[n-1] + .39*r[n-2] + 0.12*r[n-3] + 0.09*r[n-4]

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[1][1], color=color,
                             vlines_kwargs={"colors": color})

    axis[1][1].set_title("a) MA(4)")

    path = f"{image_path}.{extension}"
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
