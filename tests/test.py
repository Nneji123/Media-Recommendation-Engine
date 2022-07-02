import json
from locust import HttpUser, task, between
from functions.functions import *

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def API(self):
        sample = recommend_anime("Death Note")
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.client.post("/anime", data=json.dumps(sample.dict()), headers=headers)