from gremlin_python.driver import client, serializer
import os

ENDPOINT = os.getenv("DB_ENDPOINT")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")


def get_client():
    return client.Client(ENDPOINT, 'g', username=USERNAME, password=PASSWORD,
                         message_serializer=serializer.GraphSONSerializersV2d0())
