import time
from locust import HttpUser, task, between


class Tests(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_index(self):
        self.client.get("/")

    @task(2)
    def view_clubs_overview(self):
        self.client.get("/clubs_overview")
