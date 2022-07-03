# Importing the necessary libraries
from functions.functions import recommend_anime
# test case for the function
def test_recommend_anime():
    assert recommend_anime('Naruto') == [
        'Naruto', 'Naruto Shippuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuden') == [
        'Naruto Shippuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto: Shippuuden') == ['Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden:') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
    assert recommend_anime('Naruto Shippuuden: Shippuuden') == [
        'Naruto Shippuuden', 'Naruto: Shippuuden']
