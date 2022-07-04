import unittest
from functions.functions import recommend_manga
class TestRecommendManga:
    def test_recommend_manga(self):
        assert recommend_manga('Naruto') == [
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'],
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'], ]
