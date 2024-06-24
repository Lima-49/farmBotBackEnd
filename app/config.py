import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Config:
    QA_URL = "http://127.0.0.1:5000"
    PROD_URL = ""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def init_llm_model():
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=1000,
            verbose=True,
        )
