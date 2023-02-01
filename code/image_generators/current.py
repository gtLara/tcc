import pickle
import matplotlib.pyplot as plt

with open("data/data_dict.pkl", "rb") as file:
    data = pickle.load(file)


def current(color, dpi, image_path, extension):
    current = data[1500]['[1017:17]'][:36000]
    plt.plot(current, color=color)
    plt.title("Corrente elétrica no tempo")
    plt.xlabel("Tempo[ms]")
    plt.ylabel("Amplitude [A/A]")

    path=f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
