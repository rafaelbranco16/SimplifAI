from src.loaders import loader
from src.services.document_service import DocumentService

from src import config

class DocumentController:
    def __init__(self) -> None:
        self.document_service:DocumentService = loader.loader.resolve(config.document_service["name"])

    async def default(self):
        return await self.document_service.default()