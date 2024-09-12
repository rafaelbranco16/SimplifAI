from langchain_core.prompts import ChatPromptTemplate
'''
ChatGPT cooked this
'''
class LLMAdapter:
    '''
    Constructores
    '''
    def __init__(self) -> None:
        self.model = any

    '''
    Temporary function to test the different adapters
    '''
    async def send_prompt(self, prompt:str):
        raise NotImplementedError("This feature has not been implemented yet!")
    
    '''
    Sends a list of messages defined elsewhere to the AI
    '''
    async def send_messages(self, messages:ChatPromptTemplate):
        raise NotImplementedError("This feature has not been implemented yet!")