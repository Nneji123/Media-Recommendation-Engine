import unittest
from functions.functions import recommend_game


class TestRecommendGame(unittest.TestCase):
    def test_recommend_game(self):
        self.assertEqual(recommend_game("The Last of Us Part II"), [["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], [
                         "The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"]])
        self.assertEqual(recommend_game("The Last of Us"), [["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], [
                         "The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"]])
