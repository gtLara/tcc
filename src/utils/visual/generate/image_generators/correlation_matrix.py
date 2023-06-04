import seaborn as sns
from pathlib import Path
import pickle
import matplotlib.pyplot as plt
from src.utils.signals.correlation import get_instantaneous_crosscorrelation_matrix
from src.utils.models.trend import get_detrended_signal

plt.style.use("ggplot")

dplot = True

# Sucata às 14:49 na gaiola 17

plt.rcParams["figure.figsize"] = (15, 5)


def correlation_matrix(color, dpi, image_path, extension):

    path = Path("./data")

    with open(path/"data_dict.pkl", "rb") as file:
        data = pickle.load(file)

    interval = 100*60*7
    currents = data[1500][:interval]
    currents = currents.drop(currents.columns[17:], axis=1)
    currents = currents.apply(get_detrended_signal, axis=0)

    plt.title("Visualização de Matrix de Correlação Instantânea",
              size=17)

    correlation = get_instantaneous_crosscorrelation_matrix(currents)
    sns.heatmap(correlation, annot=True)

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)
