import json
from locust import HttpUser, task, between
import requests as re

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def testGameAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)
    
    @task(2)
    def testMovieAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)

        @task(3)
    def testAnimeAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)

        @task(4)
    def testMangaAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)

        @task(5)
    def testComicAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)

        @task(6)
    def testMusicAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)

        @task(7)
    def testBookAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)