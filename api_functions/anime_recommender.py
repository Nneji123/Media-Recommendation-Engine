# Importing the necessary libraries
from difflib import get_close_matches
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df_anime = pd.read_parquet('./data/anime.parquet', engine='fastparquet')
movie_list = list(df_anime['name'])



def recommend_anime(str):
    title = str
    title = title.lower()
    # create count matrix from this new combined column
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df_anime['genre'].values.astype('U'))

    # now compute the cosine similarity
    cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

    # correcting user input spell (close match from our movie list)
    correct_title = get_close_matches(
        title, movie_list, n=3, cutoff=0.3)[0]

    # get the index value of given movie title
    idx = df_anime['name'][df_anime['name']
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
        suggested_movie_list.append(df_anime['name'][movie_index])
    new_list_rec = []
    for j in range(len(suggested_movie_list)):
        new_list_rec.append(suggested_movie_list[j])
    return new_list_rec
