import json
from locust import HttpUser, task, between
import requests as re

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def API(self):
        value = "Call of Duty"
        sample = {"game":value}
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        test = re.post(f"http://localhost:8501/games", json=sample)