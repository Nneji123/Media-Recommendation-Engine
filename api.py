from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from typing import Optional,List
from pydantic import BaseModel
from api_functions.movie_recommender import recommendation


app = FastAPI(
    title="Recommendation Engine API",
    description="""An API that recommends movies, anime, music, favourite restaurants using machine learning.""",
    version="0.0.1", debug=True)

# Movie API Route
class MovieAPI(BaseModel):
    movie: str

@app.get("/", response_class=PlainTextResponse)
async def running():
  note = """
Recommendation Engine API 🙌🏻

Note: add "/docs" to the URL to get the Swagger UI Docs or "/redoc"
  """
  return note

@app.post("/movie")
async def movie(data: MovieAPI):
    results = recommendation(data.movie)
async def movie(data:str):
    results = recommendation(data)
    return {"data":results}

