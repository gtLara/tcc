import pickle
import matplotlib.pyplot as plt

with open("data/motor_current_samples.pkl", "rb") as file:
    data = pickle.load(file)


def current(color, dpi, image_path, extension):
    plt.plot(data, color=color)
    plt.title("Corrente elétrica no tempo")
    plt.xlabel("Tempo[ms]")
    plt.ylabel("Amplitude [A/A]")

    path = f"{image_path}.{extension}"
    plt.savefig(path, dpi=dpi, format=extension)

    plt.close()
