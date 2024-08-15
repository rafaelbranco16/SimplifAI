from src import config
from src.loaders import loader
from src.services.llm_service import LLMService


class LLMController:
    def __init__(self) -> None:
        self.service:LLMService = loader.loader.resolve(config.services["llm_service"]["name"])

    async def send_prompt(self):
        return await self.service.send_prompt()