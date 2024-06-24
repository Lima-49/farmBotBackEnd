from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import Config

class BotMessageController:
    def __init__(self):
        self.llm = Config.init_llm_model()

    def get_response(self, prompt):
        prompt_template = ChatPromptTemplate.from_template(
        """
            Você é um assistente para um gerente de uma farmácia de manipulação, chamado FarmaBot, 
            você será responsável por responder as perguntas do seu gerente 
            da maneira mais clara e precisa possível.
            
            O seu trabalho é ler o arquivo csv passado para você e responder as perguntas do seu gerente.
            com base nos dados do arquivo csv.
            
            Context: {context}
            
            Question: {input}
        """
)
        parser = StrOutputParser()
        chain = prompt_template | self.llm | parser
        response = chain.invoke({"human_input": f"{prompt}"})

        return response
