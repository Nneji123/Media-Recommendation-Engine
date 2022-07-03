import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from difflib import get_close_matches

df = pd.read_parquet("./data/comics.parquet", engine="fastparquet")
# Selecting only the first 15000 comics
n = 15000
df = df.iloc[:n]
comic_list = list(df['comic_name'])


def recommend_comics(str):
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
