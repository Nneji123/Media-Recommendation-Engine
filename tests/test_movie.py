from functions.functions import recommend_movie
# create a test function to test the code above


def test_recommend_movie():
    assert recommend_movie('The Shawshank Redemption') == ['The Godfather', 'The Godfather: Part II', 'The Dark Knight']
