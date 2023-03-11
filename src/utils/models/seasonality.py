"""
Functions for the modelling, implicit or explicit, of seasonality.
"""
import numpy as np
import pandas as pd


def get_seasonal_difference(signal: pd.Series | np.ndarray, period: int,
                            dropna: bool = True) -> \
                            pd.Series | np.ndarray:
    """
    Gets seasonal difference of arbitrary period of a signal.

    :param signal: Signal to differentiate
    :type signal: np.ndarray | np.ndarray
    :param period: Period of seasonal difference
    :type period: int
    :param dropna: Wether to remove NaN that inevitably arises from
    differencing operation, defaults to True
    :type dropna: bool
    :return: bool, defaults to True
    :rtype: np.ndarray | np.ndarray
    """

    diffed_signal = pd.Series(signal).diff(periods=period)

    if dropna:
        diffed_signal = diffed_signal.dropna()

    return diffed_signal
