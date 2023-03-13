from typing import Optional
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper
from data_processing import get_raw_csv, segment_data
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def fit_arima_model(data: pd.DataFrame,
                    order: tuple[int, int, int]) -> ARIMAResultsWrapper:
    """
    Fits arima model on data.
    :param data: DatetimeIndex indexed DataFrame containing data for model fit
    :type data: pd.Dataframe
    :param order: Order (p, i, q) of ARIMA(p, i q) model
    :type order: tuple
    :return: Fitted ARIMA model
    :rtype: ARIMAResultsWrapper
    """

    model = ARIMA(endog=data, order=order)
    model_fit = model.fit()

    return model_fit


def get_training_predictions(model: ARIMAResultsWrapper) -> np.array:
    """
    Gets training data predictions as determined by model fit.
    :param data: Fitted ARIMA model
    :type data: ARIMAResultsWrapper
    :return: Training data predictions
    :rtype: np.array
    """

    predictions = model.predict()

    return predictions


def get_test_predictions(model: ARIMAResultsWrapper,
                         data: pd.DataFrame) -> np.array:
    """
    Gets model predictions on test data which must have adjacent index to
    training data.
    :param model: Fitted ARIMA model
    :type model: ARIMAResultsWrapper
    :param data: Test data. Must have adjacent DatetimeIndex to model training
    data
    :type data: pd.DataFrame
    :return: Test data predictions
    :rtype: np.array
    """

    extended_model = model.extend(endog=data)

    predictions = extended_model.predict()

    return predictions
