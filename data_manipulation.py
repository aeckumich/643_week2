"""
This file provides functions to manipulate the data for this project, including:
- calculating the rolling average of certain statistics
"""
import pandas as pd
from calculations import batting_average


def calculate_rolling_mean(s: pd.Series, rolling_window: int) -> pd.Series:
    """
    Calculates the rolling average of a numerical statistic in the dataframe
    :param:
        s (pd.Series): Series to calculate the rolling average
        rolling_window (int): Period for the rolling average
    :return:
        s (pd.Series): Series with the rolling average calculated
    """
    s = s.rolling(rolling_window).mean()
    return s


def manipulate_data(df: pd.DataFrame, drop_opening: bool = True) -> pd.DataFrame:
    '''
    Function to manipulate the data and calculate the rolling batting average.
    :params:
        df (pd.DataFrame): dataframe to be edited
        drop_opening (bool): if True, the opening window with np.nan values are dropped. Defaults to True
    :return:
        pandas dataframe: dataframe with modifications made.
    '''
    df["BA"] = df.apply(lambda row: batting_average(row.H, row.AB), axis=1)
    df["Rolling_BA"] = calculate_rolling_mean(df["BA"], 5)
    if drop_opening:
        df.dropna(subset=["Rolling_BA"], inplace=True)

    return df
