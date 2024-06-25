from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents import create_stuff_documents_chain
from app.config import Config
import pandas as pd
import os

class BotMessageController:
    def __init__(self):
        self.llm = Config.init_llm_model()

    def create_file(self, file_name, db_folder='db'):

        if not os.path.isdir(db_folder):
            os.mkdir(db_folder)
        
        return f"{db_folder}\\{file_name}"

    def save_file(self, file_name, json_data):

        df = pd.DataFrame(json_data)
        file_data = self.create_file(file_name)
        df.to_csv(file_data, index=False)
        return file_data
    
    def get_file_by_name(self, file_name):

        file_path = os.path.join("db", file_name)
        if os.path.isfile(file_path):
            return file_path
        else:
            return None

    def get_response(self, prompt, file_name):
        """
        The `get_response` function reads a CSV file and provides 
        clear and precise responses to questions
        based on the data in the file.
        
        :param prompt: The `get_response` method takes a prompt as input,
        which is a question or query from the manager of a compounding pharmacy.
        The method uses a template to structure the prompt and then
        processes it through a language model and output parser to
        generate a response based on the data in a CSV file
        :return: The `get_response` method takes a prompt as input,
        creates a template for a chat prompt
        specific to a pharmacy manager assistant named FarmaBot,
        processes the prompt using a language model,
        and returns the response generated based on the input prompt.
        """
        response = None
        
        if file_name == '':
            prompt = ChatPromptTemplate.from_template(
                """
                    Você é um assistente para um gerente de uma farmácia de manipulação, chamado FarmaBot, 
                    você será responsável por responder as perguntas do seu gerente 
                    da maneira mais clara e precisa possível.
                    
                    O seu trabalho é ler o arquivo csv passado para você e responder as perguntas do seu gerente.
                    com base nos dados do arquivo csv.
                    
                    
                    Question: {input}
                """
            )

            parser = StrOutputParser()
            chain = prompt | self.llm | parser
            response = chain.invoke({"input": f"{prompt}"})
        
        else:
            file_path = self.get_file_by_name(file_name)
            
            loader = Config.init_csv_loader(file_path)
            data = loader.load()
            
            chain = create_stuff_documents_chain(
                llm = self.llm,
                prompt= prompt,
                output_parser= StrOutputParser()
            )
            
            response = chain.invoke({
                "input": prompt,
                "context": data  
            })


        return response
