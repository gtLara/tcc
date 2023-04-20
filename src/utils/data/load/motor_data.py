import glob
import pandas as pd


def load_normal_sample(fname: str) -> pd.DataFrame:
    """
    Loads sample of motor signals during normal motor function.
    """

    signals = pd.read_csv(fname, index_col=0,
                          infer_datetime_format=True, parse_dates=True)

    return signals


def load_anomalous_sample(fname: str) -> pd.DataFrame:
    """
    Loads sample of motor signals during anomalous motor function.
    """

    signals = pd.read_csv(fname, index_col=0,
                          infer_datetime_format=True, parse_dates=True)

    return signals


def load_normal_samples() -> list[pd.DataFrame]:
    """
    Loads all samples of motor signals during anomalous motor function.
    """

    paths = glob.glob("data/raw/normal/*")
    complete_signals = []

    for path in paths:
        complete_signals.append(load_anomalous_sample(path))

    return complete_signals


def load_anomalous_samples() -> list[pd.DataFrame]:
    """
    Loads all samples of motor signals during anomalous motor function.
    """

    paths = glob.glob("data/raw/anomalous/signals/*")
    complete_signals = []

    for path in paths:
        complete_signals.append(load_anomalous_sample(path))

    return complete_signals
