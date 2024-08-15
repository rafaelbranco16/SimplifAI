from src.loaders import loader
from src.services.document_service import DocumentService
from src.adapters.llm_adapter import LLMAdapter
from src.dto.request_dto import RequestDto

class LLMService :
    def __init__(self) -> None:
        self.llm_adapter:LLMAdapter = loader.loader.resolve("LLMAdapter")

    async def send_prompt(self, request_dto:RequestDto):
        return await self.llm_adapter.send_prompt(request_dto.prompt)
        