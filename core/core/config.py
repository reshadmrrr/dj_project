import os


class Config:
    API_KEY = "asdfasdf" or os.environ.get("API_KEY")
    BASE_URL = "127.0.0.1:1234" or os.environ.get("BASE_URL")
    AUTHOR_API_ENDPOINT = f"http://{BASE_URL}/authors"
    CONTENT_API_ENDPOINT = f"http://{BASE_URL}/contents"
