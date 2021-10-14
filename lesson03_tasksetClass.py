from locust import TaskSet, HttpUser, constant, task


class MyHTTPCat(TaskSet):

    @task
    def get_status200(self):
        self.client.get("/200")
        print("Get Status of 200")

    @task
    def get_status201(self):
        self.client.get("/201")
        print("Get Status of 201")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)
