import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders.csv_loader import CSVLoader

load_dotenv()

class Config:
    QA_URL = "http://127.0.0.1:5000"
    PROD_URL = ""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def init_llm_model():
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.3,
            max_tokens=1000,
            verbose=True,
        )
    
    @staticmethod
    def init_csv_loader(file_path):
        return CSVLoader(file_path,
                   csv_args={
                       'delimiter': ',',
                       'fieldnames': ['mes',
                                      'ano',
                                      'medicamentos',
                                      'qtd_vendas',
                                      'trimestre',
                                      'semestre',
                                      'data']
                        }
        )
