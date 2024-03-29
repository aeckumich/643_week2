import unittest
import pandas as pd
from data_loader import load_player
from data_manipulation import manipulate_data


class DataLoaderTest(unittest.TestCase):
    """
    Custom class to create test cases.
    """

    known_players = [
        "Bryce Harper",
        "Aaron Judge",
        "Carlos Correa",
        "Cody Bellinger",
        "Freddie Freeman",
    ]
    unknown_players = ["Billy Harper", "Carls", "Taylor", "frank"]

    def test_load_player_data_valid(self):
        """
        Test loading data for known players
        :return: None
        """

        for player in self.known_players:
            df = load_player(player)
            self.assertIsInstance(df, pd.DataFrame)
            self.assertEqual(
                df.shape[1], 4
            )  # Check if correct number of columns are present
            self.assertIn("Game Number", df.columns)  # Check if column renaming is done
            self.assertTrue(
                (df["AB"] >= 0).all()
            )  # Check if AB column has non-negative values

    def test_load_player_data_invalid(self):
        """
        Test function for loading data for unknown players
        :return:
        """
        for player in self.unknown_players:
            with self.assertRaises(AssertionError):
                load_player(player)


class DataManipulationTest(unittest.TestCase):
    """
    Class to create unit test cases on data manipulation file
    """
    test_player = "Freddie Freeman"
    df = load_player(test_player)

    def test_manipulate_data(self):
        """
        Test case for data_manipulation.manipulate_data().
        """
        df = manipulate_data(self.df)
        self.assertIsInstance(df, pd.DataFrame)  # test returns df
        self.assertIn("Rolling_BA", self.df)  # test rolling BA present
        self.assertIn('BA', self.df)


if __name__ == "__main__":
    unittest.main()
