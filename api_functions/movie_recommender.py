# Importing the necessary libraries
from difflib import get_close_matches
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tmdbv3api import Movie, TMDb
import imdb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df_movies = pd.read_csv('./data/movie.zip')
movie_list = list(df_movies['title'])

# creating TMDB Api Object
#later we'll use for other needs
#tmdb = TMDb()
#tmdb.api_key = '62fd9021dbeec142016bbfc8e3888baf'

#Function for movie id of any Movie
def movieiden(str):
  ia = imdb.IMDb()
  title = str
  title.lower()
# searching the name
  search = ia.search_movie(title)

# loop for printing the name and id
  for i in range((1)):
    # getting the id
    id = search[i].movieID
  # printing it
    return (id)


# This function take movie name from user, and return 10 similar type of movies.
def recommendation(str):
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
         new_list_rec.append(movieiden(suggested_movie_list[j]))
         new_list_rec.append(suggested_movie_list[j])

       return new_list_rec