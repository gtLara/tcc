import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


def ar_corr(color, dpi, image_path, extension):

    np.random.seed(42)
    size = 500
    lag = 9

    y = np.zeros(size)
    # r = np.random.random(size)

    fig, axis = plt.subplots(2, 2)

    for n in range(size):
        y[n] = 0.28*y[n-1] + np.random.random()

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[0][0], color=color,
                             vlines_kwargs={"colors": color})

    axis[0][0].set_title("a) AR(1)")

    for n in range(size):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + np.random.random()

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[0][1], color=color,
                             vlines_kwargs={"colors": color})

    axis[0][1].set_title("a) AR(2)")

    for n in range(size):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + 0.39*y[n-3] + np.random.random()

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[1][0], color=color,
                             vlines_kwargs={"colors": color})

    axis[1][0].set_title("a) AR(3)")

    for n in range(size):
        y[n] = 0.28*y[n-1] + 0.15*y[n-2] + 0.09*y[n-3] + 0.21*y[n-4] + \
               np.random.random()

    sm.graphics.tsa.plot_acf(y, lags=lag, ax=axis[1][1], color=color,
                             vlines_kwargs={"colors": color})

    axis[1][1].set_title("a) AR(4)")

    path = f"{image_path}.{extension}"
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
