from src.adapters.audio_adapter import AudioAdapter
from groq import Groq
import os
import whisper
from transformers import WhisperProcessor, WhisperForConditionalGeneration

class WhisperAdapter(AudioAdapter):
    def __init__(self) -> None:
        pass

    '''
    Generates a text from an audio_file asynchronously
    '''
    async def generate_text_from_audio(self, file_path):
        client = Groq()
        with open(file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model="whisper-large-v3", 
                response_format="json",
                language="pt",
                temperature=0.0
            )
            return transcription.text