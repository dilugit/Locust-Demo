import time

from locust import User, constant, task, between, constant_pacing


class MyUser(User):

    wait_time = constant_pacing(5)

    @task
    def launch(self):
        time.sleep(3)
        print("Total execution time is 3s, but it will wait for 5 s")

