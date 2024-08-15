from src.adapters.llm_adapter import LLMAdapter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from src import config

class GPTAdapter(LLMAdapter):
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
    
    def define_model(self):
        load_dotenv()
        self.model:ChatOpenAI = ChatOpenAI(model=config.gpt_model, api_key=os.getenv('GPT_API_KEY'))
    '''
    Sends the prompt to the OpenAI module
    '''
    async def send_prompt(self, prompt:str):
        return self.model.invoke(prompt)