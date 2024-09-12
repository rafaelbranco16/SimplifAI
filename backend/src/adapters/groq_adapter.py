from src.adapters.llm_adapter import LLMAdapter
from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langfuse.decorators import observe
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src import config
from src.loaders import load_database
from src.logger import Logger


class GroqAdapter(LLMAdapter):
    '''
    The GPT Adapter works over the LangChain
    and uses it to send a prompt

    A future plan would be to use the LangGraph instead

    @param api_key the API key to access the model
    @param model the name of the model (probably from the configuration files)
    '''
    def __init__(self) -> None:
        super().__init__()
        self.define_model()
    
    '''
    Define the model based on the configuration files
    '''
    def define_model(self):
        load_dotenv()
        self.model:ChatGroq = ChatGroq(model=config.groq_model, api_key=os.getenv('GROQ_API_KEY'))
    '''
    This is a temporary function just to test the API key

    Sends the prompt to the OpenAI module
    '''
    @observe()
    async def send_prompt(self, prompt:str):
        assist_text = '''You are a medical reviewer and I want you to return a text of this exact type:
    # Doenca: Nome da doenca
    ## Sintoma 1
    ## Sintoma 2
    Retorna somente isto sem nenhuma explicação
        '''
        prompt1 = ChatPromptTemplate.from_template(assist_text + prompt)
        chain = prompt1 | self.model | StrOutputParser()
        handler = config.langfuse_handler
        print(handler)
        return chain.invoke({},config={"callbacks":[config.langfuse_handler]})
    '''
    Sends a list of messages defined elsewhere
    '''
    async def send_messages(self, messages:ChatPromptTemplate):
        chain = messages | self.model | StrOutputParser()
        return chain.invoke({},config={"callbacks":[config.langfuse_handler]})