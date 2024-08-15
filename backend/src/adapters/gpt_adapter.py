from src.adapters.llm_adapter import LLMAdapter

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
        self.model = any
    '''
    Sends the prompt to the OpenAI module
    '''
    async def send_prompt(self):
        return {"message":"This message is from the GPT Adapter"}