from functions.functions import recommend_songs

test_song = {'name': 'The Sign', 'year': '2018'}
rec_songs = recommend_songs([test_song])
print(rec_songs)


