import numpy as np
from numpy.polynomial import Polynomial
from pykalman import KalmanFilter


def get_polynomial_trend(signal: np.array, degree: int) -> np.array:
    """
    Fits polynomial trend on time series.

    :param signal: Input signal
    :type signal: np.array
    :param degree: Degree of polynomial
    :type degree: int
    :return: Array corresponding to polynomial fit over the input signal
    :rtype: np.array
    """

    domain = np.arange(len(signal))
    polynomial = Polynomial.fit(x=domain, y=signal, deg=degree)
    _, trend = polynomial.linspace(n=len(signal))

    return trend


def get_kalman_trend(signal: np.array,
                     initial_mean: float = 0,
                     transition_variance: float = 1e-6) -> np.array:
    """
    Fits trend by using Kalman filter to smooth time series according to
    the transition equation noise variance.

    :param signal: Input signal
    :type signal: np.array
    :param degree: Variance of transition equation noise
    :return: Array corresponding to smoothed signal
    :rtype: np.array
    """

    kf = KalmanFilter(transition_matrices=[1],
                      observation_matrices=[1],
                      initial_state_mean=initial_mean,
                      initial_state_covariance=1,
                      observation_covariance=1,
                      transition_covariance=transition_variance)

    trend, _ = kf.filter(signal.values)

    return trend


def get_detrended_signal(signal: np.array, trend_degree: int = 0) -> np.array:
    """
    Removes polynomial trend from time series.

    :param signal: Input signal
    :type signal: np.array
    :param degree: Degree of trend polynomial
    :type degree: int
    :return: Detrendted signal
    :rtype: np.array
    """

    trend = get_polynomial_trend(signal, trend_degree)

    return signal - trend


# TODO: implement LOWESS and MA trend definition
