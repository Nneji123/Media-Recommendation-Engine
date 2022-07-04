import unittest
from functions.functions import recommend_game


class TestRecommendGame:
    def test_recommend_game(self):
        assert recommend_game("The Last of Us Part II") == [["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], [
                         "The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us Part II", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"]]
        assert recommend_game("The Last of Us") == [["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], [
                         "The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Multiplayer"], ["The Last of Us", "PlayStation 4", "Action-Adventure", "Horror", "Single-player"]]
