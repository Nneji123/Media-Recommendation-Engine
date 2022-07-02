import json
from locust import HttpUser, task, between
from functions.functions import *
import requests as re

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def API(self):
        sample = {"game":"Call of Duty"}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post("http://localhost:8501/games", json=sample)