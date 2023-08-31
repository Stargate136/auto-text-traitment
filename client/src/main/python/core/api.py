import requests


SERVER_URL = 'http://127.0.0.1:65432'


class APIClient:
    def __init__(self, server_url):
        self.server_url = server_url

    def send(self, task, text, **kwargs):
        response = requests.post(self.server_url + '/' + task, json={"text": text,
                                                                     **kwargs})
        return response.json()['response']


client = APIClient(SERVER_URL)


class ModelsManagerAPI:
    def __init__(self, text):
        self.text = text

    def generate_summary(self):
        return client.send("summarize", self.text)

    def generate_answer(self, question):
        return client.send("answer", self.text, question=question)
