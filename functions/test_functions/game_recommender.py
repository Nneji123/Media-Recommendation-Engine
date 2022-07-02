import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_parquet("./data/games.parquet", engine="fastparquet")

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['genre'].values.astype('U'))
cos_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)


indices=pd.Series(df.index,index=df['game_name'])
titles=df['game_name']
def recommend_game(title):
    idx = indices[title]
    similarity_scores = list(enumerate(cos_similarity[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]
    data = []
    for i in similarity_scores:
        item = []
        temp_df = df[df['game_name'] == indices.index[i[0]] ]
        item.extend(list(temp_df.drop_duplicates('game_name')['game_name'].values ))
        item.extend(list(temp_df.drop_duplicates('platform')['platform'].values ))
        item.extend(list(temp_df.drop_duplicates('game_name')['genre'].values ))
        item.extend(list(temp_df.drop_duplicates('game_name')['type'].values ))
        
        data.append(item)
    return data