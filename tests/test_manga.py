import unittest
from functions.functions import recommend_manga
class TestRecommendManga(unittest.TestCase):
    def test_recommend_manga(self):
        self.assertEqual(recommend_manga('Naruto'), [
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
            ['Naruto', 'https://myanimelist.cdn-dena.com/images/manga/3/8/8983.jpg'], ])
