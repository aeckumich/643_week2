"""
This provides a script to build a graph from a list of pandas DataFrames
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings


def build_graph(
    dfs: list[pd.DataFrame], size: tuple[float, int], filename: str
) -> None:
    """
    Build a graph from a list of pandas DataFrames and save in Graph folder.
    :params:
        - dfs: (list) a list of pandas DataFrames
        - size:  (tuple) the size of the plot (width, height)
        - filename: (str) the name of file to be saved. (Path to Graph directory provided)
    :returns:
        - None
    """
    warnings.filterwarnings("ignore", "use_inf_as_na")

    sns.set_theme()
    fig, ax = plt.subplots(figsize=size)
    df = pd.concat(dfs, ignore_index=True)
    sns.lineplot(df, x="Game Number", y="Rolling_BA", hue="Name")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.set_xlabel("Game Number")
    ax.set_ylabel("Batting Average")
    fig.suptitle("Rolling Batting Average")
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.savefig(f"Graphs/{filename}")
