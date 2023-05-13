import os
from dotenv import load_dotenv
import aioredis
from rejson import Client


load_dotenv()

class Redis():
    def __init__(self):
        """initialize  connection """
        self.REDIS_URL = os.environ['REDIS_URL']
        self.REDIS_USERNAME = os.environ['REDISUSER']
        self.REDIS_PASSWORD = os.environ['REDISPASS']
        self.connection_url = f"redis://{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"
        self.REDIS_HOST = os.environ['REDIS_HOST']
        self.REDIS_PORT = os.environ['REDIS_PORT']

    async def create_connection(self):
        self.connection = aioredis.from_url(
            self.connection_url, db=0)

        return self.connection

    def create_rejson_connection(self):
        self.redisJson = Client(host=self.REDIS_HOST,
                                port=self.REDIS_PORT, decode_responses=True, username=self.REDIS_USERNAME, password=self.REDIS_PASSWORD)

        return self.redisJson

    