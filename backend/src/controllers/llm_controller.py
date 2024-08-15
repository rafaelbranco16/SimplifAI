from src import config
from src.loaders import loader
from src.services.llm_service import LLMService
from src.dto.request_dto import RequestDto


class LLMController:
    def __init__(self) -> None:
        self.service:LLMService = loader.loader.resolve(config.services["llm_service"]["name"])

    async def send_prompt(self, request_dto:RequestDto):
        return await self.service.send_prompt(request_dto)