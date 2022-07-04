import unittest
from functions.functions import recommend_comics
# create a test case for the function above and run it with pytest
class TestRecommendComics:
    def test_recommend_comics(self):
        assert recommend_comics('Naruto') == [
            'Naruto', 'Naruto Shippuden', 'Naruto: Shippuuden']
        assert recommend_comics('Naruto Shippuden') == [
            'Naruto Shippuden', 'Naruto: Shippuuden']
        assert recommend_comics('Naruto: Shippuuden') == [
            'Naruto: Shippuuden']
        assert recommend_comics('Naruto Shippuuden') == [
            'Naruto Shippuuden', 'Naruto: Shippuuden']
        assert recommend_comics('Naruto Shippuuden:') == [
            'Naruto Shippuuden', 'Naruto: Shippuuden']
        assert recommend_comics('Naruto Shippuuden: Shippuuden') == [
            'Naruto Shippuuden', 'Naruto: Shippuuden']
