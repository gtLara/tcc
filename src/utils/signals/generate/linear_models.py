import numpy as np
import warnings
from typing import Optional


# TODO: fix cases in which poles are close to 1
def is_arma_stationary(ar_coef: np.ndarray) -> bool:
    """
    Determines wether ARMA process is stationary based on AR coefficients.

    :param num: Array containing AR coeficients in decreasing order
    (L^n, L^n-1, ... 1)
    :type ar_coef: np.ndarray
    """

    poles = np.roots([0] + ar_coef)
    smallest_pole = np.abs(poles).min()

    stationarity = (smallest_pole > 1)

    return stationarity


def generate_arma(n_samples: int, ar_coef: Optional[list[float]] = None,
                  ma_coef: Optional[list[float]] = None,
                  seed: int = 42,
                  noise_params: tuple = ("white", -1, 1)) -> np.ndarray:

    # TODO: add gaussian noise support
    """
    Generates an arbitrarily long realization of an ARMA(p, q) process with
    either white or Gaussian innovations (noise).
    """

    coef_msg = "Must include AR or MA coefficients!"
    assert ar_coef is not None or ma_coef is not None, coef_msg

    polynomial_msg = "AR and MA polynomials must be monic (first coefficient"\
                     + " equal to 1)"

    if not is_arma_stationary(ar_coef):
        warnings.warn("ARMA process not stationary.")

    if ar_coef is not None:
        assert ar_coef[-1] == 1, polynomial_msg
    if ma_coef is not None:
        assert ma_coef[-1] == 1, polynomial_msg

    if ma_coef is None:
        ma_coef = [1]

    np.random.seed(seed)

    # TODO: extract noise generation
    noise = np.random.uniform(low=min(noise_params[1:]),
                              high=max(noise_params[1:]),
                              size=n_samples)

    arma_realization = np.zeros(n_samples)

    for n in range(n_samples):

        # TODO: extract these loops
        # TODO: add stationarity warning
        if ar_coef is not None:
            for k in range(len(ar_coef)):
                if n - k > 0:
                    arma_realization[n] += ar_coef[-(k+1)] * \
                                           arma_realization[n - k]

        if ma_coef is not None:
            for k in range(len(ma_coef)):
                if n - k > -1:
                    arma_realization[n] += ma_coef[-(k+1)] * noise[n - k]

    return arma_realization
