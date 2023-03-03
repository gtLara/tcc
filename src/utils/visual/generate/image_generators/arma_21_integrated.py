import matplotlib.pyplot as plt
from src.utils.data.generate.non_linear_models import generate_arima


def arma_21_integrated(color, dpi, image_path, extension):

    ma_coef = [0.8, 1]
    ar_coef = [0.25, -0.5, 1]
    signal = generate_arima(n_samples=250, integration_order=1,
                            ar_coef=ar_coef, ma_coef=ma_coef)

    plt.plot(signal, color=color)
    plt.title("Série Temporal de Processo ARIMA(2, 1, 1)")
    plt.xlabel("Tempo")
    plt.ylabel("Magnitude")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
    plt.close()
