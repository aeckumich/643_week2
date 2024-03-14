"""
This file provides a function that loads one of the provided players CSV files and returns
them in a pandas dataframe
"""
import pandas as pd


def load_player(player_name: str) -> pd.DataFrame:
    """
    Loads one of the provided players CSV file, cleans data, calculates batting average,
    and returns them in a pandas dataframe.
        :params:
            fpath: (string) Path to the csv file
            player_name: (string) Name of the player
        :return:
            df: pd.DataFrame object
    """
    player_lookup = {
        "Bryce Harper": "data/bryce_harper.csv",
        "Freddie Freeman": "data/freddie_freeman.csv",
        "Carlos Correa": "data/carlos_correa.csv",
        "Aaron Judge": "data/aaron_judge.csv",
        "Cody Bellinger": "data/cody_bellinger.csv",
    }

    assert player_name in player_lookup, f"{player_name} not available in dateset. "
    df = pd.read_csv(player_lookup[player_name])
    relevant_columns = ["Gtm", "AB", "H"]
    df = df[relevant_columns]
    df["Name"] = player_name
    df.rename(columns={"Gtm": "Game Number"}, inplace=True)
    df.dropna(subset=["Game Number"], inplace=True)

    return df
