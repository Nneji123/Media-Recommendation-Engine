from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from typing import Optional, List
from pydantic import BaseModel
import pandas as pd
from api_functions.movie_recommender import recommend_movie
from api_functions.anime_recommender import recommend_anime
from api_functions.song_recommender import recommend_songs


app = FastAPI(
    title="Recommendation Engine API",
    description="""An API that utilises machine learning algorithms to recommends movies, anime, music, favourite restaurants using machine learning.""",
    version="0.0.1", debug=True)



favicon_path = './images/favicon.png'
@app.get('/favicon.png', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

# Home Page


@app.get("/", response_class=PlainTextResponse)
async def running():
    note = """
Recommendation Engine API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
    return note

# Movie API Route


class MovieAPI(BaseModel):
    movie: str


@app.post("/movie")
async def movie(data: MovieAPI):
    results = recommend_movie(data.movie)
    return {"data": results}


# Anime Route
class AnimeAPI(BaseModel):
    anime: str


@app.post("/anime")
async def anime(data: AnimeAPI):
    results = recommend_anime(data.anime)
    return {"data": results}

# Spotify Music API Route
class MusicAPI(BaseModel):
    music: list


@app.post("/music")
async def music(data: MusicAPI):
    """
    example input to test this route of the API:
            {
        "music": [
            {"name": "Come As You Are", "year":1991}
        ]
        }
    """
    df = pd.read_csv('./data/music.zip')
    results = recommend_songs(data.music, df)
    return {"data": results}
