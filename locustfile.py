import os
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Realistic pause between requests (1 to 3 seconds think time)
    wait_time = between(1, 3)

    @task(3)
    def normal_request(self):
        """Models regular successful user activity (75% of baseline traffic)."""
        self.client.get("/status/200", name="/status/200")

    @task(1)
    def slow_request(self):
        """Models latency-heavy operation to observe queueing and response delays."""
        self.client.get("/delay/2", name="/delay/2")

    # Set weight to 1 during the Edge Case run to trigger server errors
    @task(0)
    def edge_case_error(self):
        """Simulates intermittent HTTP 500 server failures."""
        self.client.get("/status/500", name="/status/500")