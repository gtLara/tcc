from typing import Optional
import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 6))
cmap = "magma"


def plot_stft(stft: np.ndarray, time: np.ndarray, freq: np.ndarray,
              fs: int, win_size: int, fn: str) -> None:

    plt.style.use("default")

    plt.imshow(abs(stft), cmap=cmap, extent=[time[0], time[-1], freq[-1],
               freq[0]], aspect="auto", interpolation="bilinear")

    plt.xlabel("Tempo [s]")
    plt.ylabel("Frequência [Hz]")

    plt.title(f"STFT com janela de tamanho {win_size}")
    plt.show()
    plt.savefig(fn, dpi=200)

    plt.close()


def plot_cwt(coef: np.ndarray, freqs: np.ndarray,
             n_samples: int, fs: int, title: str,
             fn: Optional[str] = None) -> None:

    scales = np.arange(1, 21, 1)

    plt.imshow(abs(coef), cmap=cmap, extent=[0, n_samples, freqs[-1],  # TODO: add time
               freqs[0]], interpolation="bilinear", aspect="auto")
    plt.gca().invert_yaxis()

    plt.xticks(np.arange(0, n_samples/fs, 2*n_samples/(20*fs)))
    plt.yticks(scales)

    plt.xlabel("Tempo [s]")
    plt.ylabel("Escala [s]")

    plt.title(title)

    plt.show()
    if fn is not None:
        plt.savefig(fn, dpi=200)

    plt.close()


def plot_wigner_ville(wigner_ville, fn):

    plt.style.use("default")

    wigner_ville.plot(default_annotation=False, show=False,
                      show_tf=False, ax=None, cmap="magma")

    plt.title("Distribuição de Wigner-Ville")
    plt.show()
    plt.savefig(fn, dpi=200)
    plt.close()
