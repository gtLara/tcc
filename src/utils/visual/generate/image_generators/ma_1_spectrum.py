from matplotlib import pyplot as plt
from src.utils.signals.generate.spectra import get_arma_spectrum


def ma_1_spectrum(color, dpi, image_path, extension):

    ma_poly = [-0.5, 1]
    ar_poly = [1]

    freqs, spectrum = get_arma_spectrum(ar_poly, ma_poly, half_spectrum=False)

    plt.plot(freqs, spectrum, color="k")
    plt.title("Densidade de Potência Espectral de Processo MA(1)")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
