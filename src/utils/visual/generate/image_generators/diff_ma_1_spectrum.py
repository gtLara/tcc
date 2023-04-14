from matplotlib import pyplot as plt
from numpy.polynomial.polynomial import polymul
from src.utils.signals.generate.spectra import get_arma_spectrum


def diff_ma_1_spectrum(color, dpi, image_path, extension):

    ma_poly = polymul([-0.5, 1], [-1, 1])
    ar_poly = [1]

    freqs, spectrum = get_arma_spectrum(ar_poly, ma_poly, half_spectrum=False)

    plt.plot(freqs, spectrum, color="k")
    plt.title("PSD of differenced MA(1) process")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
