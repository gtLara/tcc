from typing import Optional
import numpy as np
from numpy.polynomial import Polynomial

# 177500, 196000


def detect_by_linear_inclination(signal: np.ndarray[float],
                                 shutdown_mask: Optional[np.ndarray[bool]],
                                 window_length: int = 45000,
                                 threshold: float = 0.0001) -> \
                                 np.ndarray[bool]:

    anomaly_indices = np.zeros(len(signal), dtype=bool)

    for i in range(len(signal)//window_length):

        indices = slice(i*window_length, (i+1)*window_length)

        if sum(shutdown_mask[indices]) > 0.2*window_length:
            continue

        subsignal = signal[indices]
        poly = Polynomial.fit(x=np.arange(window_length), y=subsignal, deg=1)

        print(poly.deriv().coef[0])
        if poly.deriv().coef[0] > threshold:
            anomaly_indices[indices] = True

    return anomaly_indices
