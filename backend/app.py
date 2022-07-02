from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from typing import Optional, List
from pydantic import BaseModel
import pandas as pd
from api_functions.movie_recommender import recommend_movie
from api_functions.anime_recommender import recommend_anime
from api_functions.song_recommender import recommend_songs
from api_functions.book_recommender import recommend_book
from api_functions.game_recommender import recommend_game
from api_functions.manga_recommender import recommend_manga

app = FastAPI(
    title="Recommendation Engine API",
    description="""An API that utilises machine learning algorithms to recommends movies, anime, music, books and comics.""",
    version="0.0.1",
    debug=True,
)


favicon_path = "./images/favicon.png"


@app.get("/favicon.png", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


# Home Page


@app.get("/", response_class=PlainTextResponse)
async def home():
    note = """
Recommendation Engine API 🙌🏻

This API recommends content such as games, movies, music, books and even anime!

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
    return note


# Movie API Route


class RecommenderAPI(BaseModel):
    movie: str
    anime: str
    music: list
    book: str
    game: str
    manga: str


@app.post(
    "/movie",
    summary="This endpoint recommends movies based on the movie genre and name.",
)
async def movie(data: RecommenderAPI):
    """
    This endpoint takes only one input, name of the movie.
    """
    results = recommend_movie(data.movie)
    return {"data": results}


# Anime Route


@app.post(
    "/anime",
    summary="This endpoint recommends anime based on the anime genre and name.",
)
async def anime(data: RecommenderAPI):
    """
    This endpoint takes only one input, name of the anime.

    """
    results = recommend_anime(data.anime)
    return {"data": results}


# Spotify Music API Route


@app.post("/music", summary="This endpoint recommends songs from user input")
async def music(data: RecommenderAPI):
    """
    This endpoint takes the following input
    name: Name of the Song
    year:Year the song was released

    example input to test this route of the API:
            {
        "music": [
            {"name": "Come As You Are", "year":1991}
        ]
        }
    """
    df = pd.read_parquet("./data/music.parquet", engine="fastparquet")
    results = recommend_songs(data.music, df)
    return {"data": results}


# Books Endpoint


@app.post("/books", summary="This endpoint recommends books from user input")
async def music(data: RecommenderAPI):
    """
    This endpoint takes the following input
    name: Name of the book
    """
    results = recommend_book(data.book)
    return {"data": results}


# Games API Route


@app.post("/games", summary="This endpoint recommends games from user input")
async def games(data: RecommenderAPI):
    """
    This endpoint takes the following input
    name: Name of the game
    """
    results = recommend_game(data.game)
    return {"data": results}


# Manga API Route


@app.post("/manga", summary="This endpoint recommends manga from user input")
async def games(data: RecommenderAPI):
    """
    This endpoint takes the following input
    name: Name of the manga
    """
    results = recommend_manga(data.manga)
    return {"data": results}
