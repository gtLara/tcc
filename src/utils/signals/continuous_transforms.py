import pywt
from scipy.signal import stft
from tftb.processing import WignerVilleDistribution


def get_short_time_fourier_transform(signal, fs, win_size):

    freqs, time, coefs = stft(signal, fs=fs, nperseg=win_size)

    return freqs, time, coefs


def get_continuous_wavelet_transform(signal, wavelet, scales):

    coef, freqs = pywt.cwt(signal, scales, wavelet)

    return freqs, coef


def get_wigner_ville_transform(signal):

    wigner_ville = WignerVilleDistribution(signal[:len(signal) - 1])
    wigner_ville.run()

    return wigner_ville
