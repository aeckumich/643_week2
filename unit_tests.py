import unittest
import pandas as pd
from data_loader import load_player


class DataLoaderTest(unittest.TestCase):
    known_players = [
        "Bryce Harper",
        "Aaron Judge",
        "Carlos Correa",
        "Cody Bellinger",
        "Freddie Freeman",
    ]

    unknown_players = ['Billy Harper', 'Carls', 'Taylor']

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
        for player in self.unknown_players:
                with self.assertRaises(AssertionError):
                    load_player(player)



if __name__ == "__main__":
    unittest.main()