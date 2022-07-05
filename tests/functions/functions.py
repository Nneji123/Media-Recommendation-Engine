# Importing the necessary libraries
import os
from decouple import config
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import difflib
from collections import defaultdict
from difflib import get_close_matches
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from scipy.spatial.distance import cdist

import warnings
warnings.filterwarnings("ignore")


def recommend_anime(str):
    """This function performs the following actions:
    1. Reads the anime.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given anime title.
    5. Pairwise similarity scores of all animes with that anime.
    6. Sort the anime based on similarity scores.
    7. Suggested anime are stored into a list.


    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar anime from the dataset.

    """
    df_anime = pd.read_parquet(
        './data/anime.parquet', engine='fastparquet', columns=["name", "genre"])
    movie_list = list(df_anime['name'])
    title = str
    title = title.lower()

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df_anime['genre'].values.astype('U'))

    # Set to true to get more recommendations
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    correct_title = get_close_matches(
        title, movie_list, n=3, cutoff=0.3)[0]

    idx = df_anime['name'][df_anime['name']
                           == correct_title].index[0]

    sim_score = list(enumerate(cos_similarity[idx]))
    #
    sim_score = sorted(
        sim_score, key=lambda x: x[1], reverse=True)[0:15]

    suggested_movie_list = []
    for i in sim_score:
        movie_index = i[0]
        suggested_movie_list.append(df_anime['name'][movie_index])
    new_list_rec = []
    for j in range(len(suggested_movie_list)):
        new_list_rec.append(suggested_movie_list[j])
    return new_list_rec


def recommend_book(bk_name):
    """
    This function performs the following actions:
    1. Reads the book.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given book title.
    5. Pairwise similarity scores of all books with that book.
    6. Sort the book based on similarity scores.
    7. Suggested book are stored into a list.

    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar books from the dataset.


    """
    # fetch Book Index
    dfbooks_rating = pd.read_parquet("./data/books.parquet", engine="fastparquet", columns=[
                                     "User-ID", "Book-Rating", "Book-Title", "Image-URL-M", "Book-Author"])
    dfbooks = pd.read_parquet("./data/books.parquet", engine="fastparquet")
    dfbooks_rating_count = dfbooks_rating.groupby(
        'User-ID').agg(['count'])['Book-Rating'].reset_index()
    # Count value more than 200
    xdfbooks_rating_userID = dfbooks_rating_count[dfbooks_rating_count['count'] > 200]

    # Filteing the required User of Dataset (Count more than 200 )
    xdfbooks_rating = dfbooks_rating[dfbooks_rating['User-ID'].isin(
        xdfbooks_rating_userID['User-ID'].tolist())]

    xdfbooks_count = xdfbooks_rating.groupby(
        'Book-Title').agg(['count'])['Book-Rating'].reset_index()
    xdfbooks_popular = xdfbooks_count[xdfbooks_count['count'] >= 50]
    xdfbooks_famous = xdfbooks_rating[xdfbooks_rating['Book-Title'].isin(
        xdfbooks_popular['Book-Title'].tolist())].drop_duplicates()

    xdf_pivot = xdfbooks_famous.pivot_table(
        index='Book-Title', columns='User-ID', values='Book-Rating')
    xdf_pivot.fillna(0, inplace=True)
    similarity_score = cosine_similarity(xdf_pivot, dense_output=False)
    indx = np.where(xdf_pivot.index == bk_name)[0][0]
    similarity_score = cosine_similarity(xdf_pivot)
    similar_books = sorted(
        list(enumerate(similarity_score[indx])), key=lambda x: x[1], reverse=True)[1:11]
    data = []
    for i in similar_books:
        item = []
        temp_df = dfbooks[dfbooks['Book-Title'] == xdf_pivot.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates(
            'Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data


def recommend_comics(str):
    """
    This function performs the following actions:
    1. Reads the comics.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given comic title.
    5. Pairwise similarity scores of all comics with that comic.
    6. Sort the comic based on similarity scores.
    7. Suggested comic are stored into a list.

    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar comics from the dataset.
    """
    df = pd.read_parquet("./data/comics.parquet",
                         engine="fastparquet", columns=["comic_name", "Rating"])
    # Selecting only the first 15000 comics
    n = 15000
    df = df.iloc[:n]
    comic_list = list(df['comic_name'])
    title = str
    title = title.lower()
    # create count matrix from this new combined column
    cv = TfidfVectorizer()
    tfidf_matrix = cv.fit_transform(df['Rating'])

    # now compute the cosine similarity
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    # correcting user input spell (close match from our movie list)
    correct_title = get_close_matches(
        title, comic_list, n=3, cutoff=0.3)[0]

    # get the index value of given movie title
    idx = df['comic_name'][df['comic_name']
                           == correct_title].index[0]

    # pairwise similarity scores of all movies with that movie
    sim_score = list(enumerate(cos_similarity[idx]))
    # sort the movie based on similarity scores
    sim_score = sorted(
        sim_score, key=lambda x: x[1], reverse=True)[0:15]
    # suggested movies are storing into a list
    suggested_comic_list = []
    for i in sim_score:
        movie_index = i[0]
        suggested_comic_list.append(df['comic_name'][movie_index])
    data = []
    for j in range(len(suggested_comic_list)):
        data.append(suggested_comic_list[j])

    return data


def recommend_game(title):
    """
    This function performs the following actions:
    1. Reads the games.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given game title.
    5. Pairwise similarity scores of all games with that game.
    6. Sort the game based on similarity scores.
    7. Suggested game are stored into a list.

    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar games from the dataset.

    """
    df = pd.read_parquet("./data/games.parquet", engine="fastparquet",
                         columns=["genre", "game_name", "platform", "type"])

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['genre'].values.astype('U'))
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df.index, index=df['game_name'])
    titles = df['game_name']
    idx = indices[title]
    similarity_scores = list(enumerate(cos_similarity[idx]))
    similarity_scores = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]
    data = []
    for i in similarity_scores:
        item = []
        temp_df = df[df['game_name'] == indices.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates(
            'game_name')['game_name'].values))
        item.extend(list(temp_df.drop_duplicates(
            'platform')['platform'].values))
        item.extend(list(temp_df.drop_duplicates('game_name')['genre'].values))
        item.extend(list(temp_df.drop_duplicates('game_name')['type'].values))

        data.append(item)
    return data


def recommend_manga(title):
    """
    This function performs the following actions:
    1. Reads the manga.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given manga title.
    5. Pairwise similarity scores of all manga with that manga.
    6. Sort the manga based on similarity scores.
    7. Suggested manga are stored into a list.

    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar manga from the dataset.


    """
    df = pd.read_parquet("./data/manga.parquet", engine="fastparquet",
                         columns=["Genre", "Name", "img-link"])

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['Genre'].values.astype('U'))
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df.index, index=df['Name'])
    titles = df['Name']

    idx = indices[title]
    similarity_scores = list(enumerate(cos_similarity[idx]))
    similarity_scores = sorted(
        similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]
    data = []
    for i in similarity_scores:
        item = []
        temp_df = df[df['Name'] == indices.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Name')['Name'].values))
        item.extend(list(temp_df.drop_duplicates('Name')['img-link'].values))
        data.append(item)
    return data


# This function take movie name from user, and return 10 similar type of movies.
def recommend_movie(str):
    """
    This function performs the following actions:
    1. Reads the movies.parquet file and gets the correct title name using difflib.
    2. Create count matrix from this new combined column.
    3. Compute the cosine similarity.
    4. Get the index value of given movie title.
    5. Pairwise similarity scores of all movies with that movie.
    6. Sort the movie based on similarity scores.
    7. Suggested movies are stored into a list.

    Args:
        param1: takes one input of type string

    Returns:
        list: Returns a list of similar movies from the dataset.



    """
    df_movies = pd.read_parquet(
        './data/movie.parquet', engine='fastparquet', columns=["genres", "title"])
    movie_list = list(df_movies['title'])

    title = str
    title = title.lower()
    # create count matrix from this new combined column
    cv = TfidfVectorizer()
    tfidf_matrix = cv.fit_transform(df_movies['genres'])

    # now compute the cosine similarity
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    # correcting user input spell (close match from our movie list)
    correct_title = get_close_matches(
        title, movie_list, n=3, cutoff=0.3)[0]

    # get the index value of given movie title
    idx = df_movies['title'][df_movies['title']
                             == correct_title].index[0]

    # pairwise similarity scores of all movies with that movie
    sim_score = list(enumerate(cos_similarity[idx]))
    # sort the movie based on similarity scores
    sim_score = sorted(
        sim_score, key=lambda x: x[1], reverse=True)[0:15]
    # suggested movies are storing into a list
    suggested_movie_list = []
    for i in sim_score:
        movie_index = i[0]
        suggested_movie_list.append(df_movies['title'][movie_index])
    new_list_rec = []
    for j in range(len(suggested_movie_list)):
        new_list_rec.append(suggested_movie_list[j])

    return new_list_rec


data = pd.read_parquet("./data/music.parquet", engine="fastparquet")
SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')

song_cluster_pipeline = Pipeline([('scaler', StandardScaler()),
                                  ('kmeans', KMeans(n_clusters=20,
                                                    verbose=False))
                                  ], verbose=False)

X = data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                           client_secret=SPOTIFY_CLIENT_SECRET))


def find_song(name, year):

    song_data = defaultdict()
    results = sp.search(q='track: {} year: {}'.format(name, year), limit=1)
    if results['tracks']['items'] == []:
        return None

    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    song_data['name'] = [name]
    song_data['year'] = [year]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['popularity'] = [results['popularity']]

    for key, value in audio_features.items():
        song_data[key] = value

    return pd.DataFrame(song_data)


number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


def get_song_data(song, spotify_data):

    try:
        song_data = spotify_data[(spotify_data['name'] == song['name'])
                                 & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data

    except IndexError:
        return find_song(song['name'], song['year'])


def get_mean_vector(song_list, spotify_data):

    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print('Warning: {} does not exist in Spotify or in database'.format(
                song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)

    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)


def flatten_dict_list(dict_list):

    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []

    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)

    return flattened_dict


def recommend_songs(song_list, spotify_data, n_songs=10):
    """
    To use this function properly make sure you set the environment variables in the .env file.
    This function performs the following actions:
    1. Gets the mean vector of the song list.
    2. Gets the mean vector of the song cluster.
    3. Computes the cosine similarity.
    4. Gets the index value of given song cluster.
    5. Pairwise similarity scores of all song clusters with that song cluster.
    6. Sort the song cluster based on similarity scores.
    7. Suggested songs are stored into a list.

    Args:
        param1: takes one input of type list

    Returns:
        list: Returns a list of similar songs from the dataset.
    """

    metadata_cols = ['name', 'year', 'artists']
    song_dict = flatten_dict_list(song_list)

    song_center = get_mean_vector(song_list, spotify_data)
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(spotify_data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])

    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    return rec_songs[metadata_cols].to_dict(orient='records')
