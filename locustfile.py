from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def normal_request(self):
        self.client.get("/status/200")

    @task(1)
    def slow_request(self):
        self.client.get("/delay/2")