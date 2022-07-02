import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics.pairwise import cosine_similarity

def recommend_book(bk_name):
    # fetch Book Index
    dfbooks_rating = pd.read_parquet("./data/books.parquet")
    dfbooks = pd.read_parquet("./data/books.parquet")
    dfbooks_rating_count = dfbooks_rating.groupby('User-ID').agg(['count'])['Book-Rating'].reset_index()
    xdfbooks_rating_userID = dfbooks_rating_count[dfbooks_rating_count['count'] > 200] # Count value more than 200

    # Filteing the required User of Dataset (Count more than 200 )
    xdfbooks_rating = dfbooks_rating[dfbooks_rating['User-ID'].isin(xdfbooks_rating_userID['User-ID'].tolist() )]

    xdfbooks_count = xdfbooks_rating.groupby('Book-Title').agg(['count'])['Book-Rating'].reset_index()
    xdfbooks_popular = xdfbooks_count[xdfbooks_count['count'] >= 50]
    xdfbooks_famous = xdfbooks_rating[xdfbooks_rating['Book-Title'].isin(xdfbooks_popular['Book-Title'].tolist() )].drop_duplicates()


    xdf_pivot = xdfbooks_famous.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
    xdf_pivot.fillna(0, inplace=True)
    similarity_score = cosine_similarity(xdf_pivot)
    indx = np.where(xdf_pivot.index == bk_name)[0][0]
    similarity_score = cosine_similarity(xdf_pivot)
    similar_books = sorted(list(enumerate(similarity_score[indx])), key=lambda x:x[1], reverse=True)[1:11]
    data = []
    for i in similar_books:
        item = []
        temp_df = dfbooks[dfbooks['Book-Title'] == xdf_pivot.index[i[0]] ]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values ))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values ))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values ))
        
        data.append(item)
    
    return data