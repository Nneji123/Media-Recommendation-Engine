from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from pydantic import BaseModel
import pandas as pd
from functions.models import *
from functions.functions import *

app = FastAPI(
    title="Recommendation Engine API",
    description="""An API that utilises machine learning algorithms to recommends movies, anime, music, books, comics, manga and games.""",
    version="0.0.1",
    debug=True,
    docs_url="/"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


favicon_path = "./images/favicon.png"


@app.get("/favicon.png", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


# Home Page


@app.get("/home", response_class=PlainTextResponse, tags=["home"])
async def home():
    note = """
Recommendation Engine API 🙌🏻

This API recommends content such as games, movies, music, books and even anime!

Note: add "/redoc" to get the complete documentation.
  """
    return note


# Movie API Route

@app.post(
    "/movie",
    summary="This endpoint recommends movies based on the movie genre and name.",
    tags=["movies"]
)
async def movie(data: MovieAPI):
    """
    This endpoint takes only one input, name of the movie.
    """
    results = recommend_movie(data.movie)
    return {"data": results}


# Anime Route


@app.post(
    "/anime",
    summary="This endpoint recommends anime based on the anime genre and name.",
    tags=["anime"]
)
async def anime(data: AnimeAPI):
    """
    This endpoint takes only one input, name of the anime.

    """
    results = recommend_anime(data.anime)
    return {"data": results}


# Spotify Music API Route


@app.post("/songs", summary="This endpoint recommends songs from user input",tags=["songs"])
async def songs(data: SongsAPI):
    """
    This endpoint takes the following input
    name: Name of the Song
    year:Year the song was released

    example input to test this route of the API:
            {
        "songs": [
            {"name": "Come As You Are", "year":1991}
        ]
        }
    """
    df = pd.read_parquet("./data/music.parquet", engine="fastparquet")
    results = recommend_songs(data.songs, df)
    return {"data": results}


# Books Endpoint


@app.post("/books", summary="This endpoint recommends books from user input",tags=["books"])
async def music(data: BookAPI):
    """
    This endpoint takes the following input
    name: Name of the book
    """
    results = recommend_book(data.book)
    return {"data": results}


# Games API Route


@app.post("/games", summary="This endpoint recommends games from user input",tags=["games"])
async def games(data: GamesAPI):
    """
    This endpoint takes the following input
    name: Name of the game
    """
    results = recommend_game(data.game)
    return {"data": results}


# Manga API Route


@app.post("/manga", summary="This endpoint recommends manga from user input",tags=["manga"])
async def manga(data: MangaAPI):
    """
    This endpoint takes the following input
    name: Name of the manga
    """
    results = recommend_manga(data.manga)
    return {"data": results}

# Comics API Route


@app.post("/comics", summary="This endpoint recommends marvel comics from user input",tags=["comics"])
async def comics(data: ComicsAPI):
    """
    This endpoint takes the following input
    name: Name of the manga
    """
    results = recommend_comics(data.comic)
    return {"data": results}
