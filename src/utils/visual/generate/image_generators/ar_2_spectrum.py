from matplotlib import pyplot as plt
from src.utils.signals.generate.spectra import get_arma_spectrum


def ar_2_spectrum(color, dpi, image_path, extension):

    ma_poly = [1]
    ar_poly = [-0.25, 0.5, 1]

    freqs, spectrum = get_arma_spectrum(ar_poly, ma_poly, half_spectrum=False)

    plt.plot(freqs, spectrum, color="k")
    plt.title("PSD of AR(2) process")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
