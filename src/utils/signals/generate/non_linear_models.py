from typing import Optional
import numpy as np
from src.utils.signals.generate.linear_models import generate_arma


def generate_arima(n_samples: int, integration_order: int,
                   ar_coef: Optional[list[float]] = None,
                   ma_coef: Optional[list[float]] = None,
                   seed: int = 42,
                   noise_params: tuple = ("white", -1, 1)) -> np.ndarray:

    """
    Generates an arbitrarily long realization of an ARIMA(p, i, q) process with
    either white or Gaussian innovations (noise).
    """

    arma_signal = generate_arma(n_samples, ar_coef, ma_coef, seed,
                                noise_params)

    for i in range(integration_order):
        if i == 0:
            arima_signal = np.cumsum(arma_signal)
        else:
            arima_signal = np.cumsum(arima_signal)

    return arima_signal
