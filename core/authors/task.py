import requests
import time
from datetime import datetime, timedelta
from celery import shared_task
from core.config import Config


@shared_task
def fetch_author_api_data(rate=5):

    url = Config.AUTHOR_API_ENDPOINT
    headers = {"x-api-key:": Config.API_KEY}

    interval = timedelta(hours=1) / rate
    start_time = datetime.utcnow().replace(second=0, microsecond=0)

    while datetime.utcnow() < start_time + interval:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            print(data)  # do something with the data

            print(f"Fetched API data at {datetime.utcnow()}")
        except Exception as e:
            print(f"API fetch error: {e}")

        sleep_time = (start_time + interval - datetime.utcnow()).total_seconds()
        time.sleep(max(0, sleep_time))
