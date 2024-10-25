from fastapi import UploadFile
from src.loaders import loader
from src.services.audio_service import AudioService
from src import config
import json


class AudioController:
    def __init__(self) -> None:
        self.service:AudioService = loader.loader.resolve(config.audio_service["name"])

    async def generate_text_from_audio(self, file: UploadFile):
        return await self.service.generate_text_from_audio(file)
    
    async def generate_entry_note_text(self, text: str):
        return json.loads(await self.service.generate_entry_note_from_audio(text))
