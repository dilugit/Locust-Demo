from locust import SequentialTaskSet, HttpUser, constant, task


class MySeqTask(SequentialTaskSet):

    @task
    def get_status500(self):
        self.client.get("/500")
        print("Get Status of 500")

    @task
    def get_status200(self):
        self.client.get("/200")
        print("Get Status of 200")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)
