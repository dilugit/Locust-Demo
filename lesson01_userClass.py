from locust import User, task, constant


class MyFirstTest(User):
    weight = 2
    # wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL1")

    @task
    def search(self):
        print("Searching1")


class MySecondTest(User):
    weight = 2
    # wait_time = constant(1)

    @task
    def launch2(self):
        print("Launching the URL2")

    @task
    def search2(self):
        print("Searching2")
