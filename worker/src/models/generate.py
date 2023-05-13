from re import T
from gpt4allj.langchain import GPT4AllJ
from langchain import PromptTemplate, LLMChain
import os
from dotenv import load_dotenv
import requests
import json
from ..redis.config import Redis
from ..schema.chat import Message
from ..redis.producer import Producer

load_dotenv()
redis = Redis()



class GPT():
    def __init__(self, model_path):
        self.llm = GPT4AllJ(model=model_path, instructions='basic', seed=-1,
                    n_threads=-1,
                    n_predict=1000,
                    top_k=1000,
                    top_p=1,
                    temp=0.6,
                    repeat_penalty=1.1,
                    repeat_last_n=128,
                    n_batch=10)
        # self.json_client = redis.create_rejson_connection()
        # redis_client = redis.create_connection()
        # self.producer = Producer(redis_client)

    def langchain(self, prompt): 
        template = """Question: {question}

            Answer:"""

        prompter = PromptTemplate(template=template, input_variables=['question'])

        llm_chain = LLMChain(prompt=prompter,llm=self.llm)
        answer = llm_chain.run(prompt)
        while True:
            if answer:
                return answer
            
        