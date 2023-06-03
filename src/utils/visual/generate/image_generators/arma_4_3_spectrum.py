from matplotlib import pyplot as plt
from src.utils.signals.generate.spectra import get_arma_spectrum


def arma_4_3_spectrum(color, dpi, image_path, extension):

    ma_poly = [-0.175, 0.8, 1]
    ar_poly = [-0.75, 0.125, .5, 1]

    freqs, spectrum = get_arma_spectrum(ar_poly, ma_poly, half_spectrum=False)

    plt.plot(freqs, spectrum, color="k")
    plt.title("Densidade de Potência Espectral de Processo ARMA(4, 3)")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
