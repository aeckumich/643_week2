"""
This file stores functions for custom baseball statistic calculations
"""


def batting_average(hits: int, at_bats: int) -> float:
    """
    Calculates a players batting average defined as how many hits divided by how many at bats.
    :params:
        hits: (int) number of hits
        at_bats: (int) number of at bats
    :return:
        bating_average: (float) the batting average
    """

    bating_average = hits / at_bats

    return bating_average
