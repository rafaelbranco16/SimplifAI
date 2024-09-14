from fastapi import UploadFile
from src.loaders import loader
from src.services.audio_service import AudioService
from src import config


class AudioController:
    def __init__(self) -> None:
        self.service:AudioService = loader.loader.resolve(config.audio_service["name"])

    async def generate_text_from_audio(self, file: UploadFile):
        return await self.service.generate_text_from_audio(file)