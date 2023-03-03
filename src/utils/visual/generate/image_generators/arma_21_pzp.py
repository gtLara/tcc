import matplotlib.pyplot as plt
from src.utils.visual.plot.pole_zero_diagram import pole_zero_plot


def arma_21_pzp(color, dpi, image_path, extension):

    ma_coef = [0.8, 1]
    ar_coef = [0.25, -0.5, 1]

    pole_zero_plot(ma_coef, ar_coef)
    plt.title(r"Diagrama de Polos e Zeros em $L$ de Processo ARMA(2, 1)")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
