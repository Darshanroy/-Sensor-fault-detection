import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """

    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass


class DataPreprocessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocesses the data.
    """

    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values, and converts the data type to float.
        """
        try:
            data = data.drop('Unnamed: 0',axis=1)

            def get_cols_zero_std(df : pd.DataFrame):

                cols_to_drop: list = []
                num_cols = [i for i in df.columns[1:] if df[i].dtype != "O"]
                for i in df.columns[1:]:
                    if df[i].std() ==0:
                        cols_to_drop.append(i)
                return cols_to_drop
            
            def get_reduntant_col(df: pd.DataFrame, missing_thresh = .7):
                cols_missing_ratio = df.isnull().sum().div(df.shape[0])
                cols_to_drop = list(cols_missing_ratio[cols_missing_ratio > missing_thresh].index)
                return cols_to_drop
            
            cols_drop_1 = get_cols_zero_std(df = data)
            cols_drop_2 = get_reduntant_col(data, missing_thresh= .7)
            cols_to_drop = cols_drop_1 +cols_drop_2 

            data = data.drop(cols_to_drop, axis = 1)
            print(data.head())

            return data
        except Exception as e:
            logging.error(e)
            raise e


class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """

    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        """
        Divides the data into train and test data.
        """
        try:
            X = data.drop("Good/Bad", axis=1)
            y = data["Good/Bad"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(e)
            raise e


class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """

    def __init__(self, data: pd.DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.df = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data based on the provided strategy"""
        return self.strategy.handle_data(self.df)