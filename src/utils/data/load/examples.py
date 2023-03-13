from typing import Optional
import pickle
import numpy as np
import pandas as pd
from scipy.signal import decimate
from scipy.ndimage import uniform_filter1d


def get_seasonal_data(decimation_factor: int = 10,
                      moving_average_win_size: Optional[int] = None) -> pd.Series | np.ndarray:
    """
    Gets example of seasonal data.

    """

    with open("data/data_dict.pkl", "rb") as file:
        data = pickle.load(file)

    start = pd.to_datetime("2021-05-29 16:32")
    end = pd.to_datetime("2021-05-29 16:40")
    raw_signal = data[1700]["[1017:3]"][start:end]

    if decimation_factor > 1:
        signal = decimate(raw_signal, decimation_factor)

    if moving_average_win_size:
        signal = uniform_filter1d(signal, size=moving_average_win_size)

    return signal
