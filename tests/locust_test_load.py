import json
from locust import HttpUser, task, between
import requests as re

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def testGameAPI(self):
        value = "Call of Duty"
        sample = {"game":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/games", data= json.dumps(sample), headers=headers)
    
    @task(2)
    def testMovieAPI(self):
        value = "Toy Story"
        sample = {"movie":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/movie", data= json.dumps(sample), headers=headers)

    @task(3)
    def testAnimeAPI(self):
        value = "Death Note"
        sample = {"anime":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/anime", data= json.dumps(sample), headers=headers)

    @task(4)
    def testMangaAPI(self):
        value = "Crush On You"
        sample = {"manga":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/manga", data= json.dumps(sample), headers=headers)

    @task(5)
    def testComicAPI(self):
        value = "A Year of Marvels: August Infinite Comic"
        sample = {"comic":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/comics", data= json.dumps(sample), headers=headers)

    @task(6)
    def testMusicAPI(self):
        value = {"name":"Come As You Are", "year":1991}
        sample = {"music":[value]}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/music", data= json.dumps(sample), headers=headers)

    @task(7)
    def testBookAPI(self):
        value = "1984"
        sample = {"book":value}
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/books", data= json.dumps(sample), headers=headers)