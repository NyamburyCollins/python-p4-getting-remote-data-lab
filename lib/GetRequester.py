import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # __define-ocg__: Fetching raw byte content from HTTP response
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Parses the JSON content from the response
        response = requests.get(self.url)
        return response.json()
