import numpy as np


def evaluate_polynomial_freq_response(poly: list | np.ndarray,
                                      freq: float) -> float:
    """
    Evaluates frequency response of polynomial transfer function on a
    specific frequency value.

    Polynomial coefficients are informed in
    decreasing order, so the polynomial

        2 z^-2 + z^-1 - 1

    Would be informed as

        poly = [2, 1, -1]

    :param poly: Coefficients of polynomial transfer function defined over
    z^-1
    :type poly: list | np.ndarray
    :param freq: Frequency value from which to evaluate transfer function
    :return: Value of the given transfer function evaluated on the
    given frequency value
    :rtype: float
    """
    spectral_sum = 1
    for n, coef in enumerate(np.flip(poly)[1:]):
        spectral_sum += -coef * np.exp(-(n+1)*freq*complex(imag=1))

    return np.abs(spectral_sum)**2


def get_polynomial_spectrum(poly: list | np.ndarray,
                            half_spectrum: bool = True) -> tuple[np.ndarray,
                                                                 np.ndarray]:
    """
    Gets spectrum of polynomial transfer function.

    Polynomial coefficients are informed in
    decreasing order, so the polynomial

        2 z^-2 + z^-1 - 1

    Would be informed as

        poly = [2, 1, -1]


    :param poly: Coefficients of polynomial transfer function defined over
    z^-1
    :type poly: list | np.ndarray
    :param half_spectrum: Wether the spectrum should be over [-pi, pi] or
    [0, pi], defaults to True
    :type half_spectrum: bool
    :return: Frequency range and spectrum of polynomial transfer function
    :rtype: tuple[np.ndarray, np.ndarray]
    """

    initial_freq = 0 if half_spectrum else -np.pi
    final_freq = np.pi

    freq_range = np.arange(initial_freq, final_freq, 0.01)
    spectrum = np.array([evaluate_polynomial_freq_response(poly,
                         freq) for freq in freq_range])

    return freq_range, spectrum


def get_arma_spectrum(ar_poly: list | np.ndarray,
                      ma_poly: list | np.ndarray,
                      noise_variance: float = 1,
                      half_spectrum: bool = True) -> tuple[np.ndarray,
                                                           np.ndarray]:
    """
    Gets spectrum of an ARMA transfer function.

    Polynomial coefficients are informed in
    decreasing order, so the polynomial

        2 z^-2 + z^-1 - 1

    Would be informed as

        poly = [2, 1, -1]


    :param ar_poly: Coefficients of autoregressive polynomial transfer function
    defined over z^-1
    :type ar_poly: list | np.ndarray
    :param ma_poly: Coefficients of moving average polynomial transfer function
    defined over z^-1
    :type ma_poly: list | np.ndarray
    :param noise_variance: Variance of white noise input
    :type noise_variace: float, defaults to 1
    :param half_spectrum: Wether the spectrum should be over [-pi, pi] or
    [0, pi], defaults to True
    :type half_spectrum: bool
    :return: Frequency range and spectrum of ARMA transfer function
    :rtype: tuple[np.ndarray, np.ndarray]
    """

    scale_factor = (2*np.pi)/noise_variance

    freqs, ma_spectrum = get_polynomial_spectrum(ma_poly, half_spectrum)
    freqs, ar_spectrum = get_polynomial_spectrum(ar_poly, half_spectrum)

    arma_spectrum = scale_factor*(ma_spectrum/ar_spectrum)

    return freqs, arma_spectrum
