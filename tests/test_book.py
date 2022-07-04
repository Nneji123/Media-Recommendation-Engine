import unittest
from functions.functions import recommend_book

# create a test case


class TestRecommendBook:
    def test_recommend_book(self):
        assert recommend_book('The Great Gatsby') == [['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], [
                         'The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg'], ['The Great Gatsby', 'F. Scott Fitzgerald', 'https://images-na.ssl-images-amazon.com/images/I/51Z%2B1t%2B7QTL._SX331_BO1,204,203,200_.jpg']]
