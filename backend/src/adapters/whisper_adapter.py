import whisper
from src.adapters.audio_adapter import AudioAdapter
from dotenv import load_dotenv
from groq import Groq

class WhisperAdapter(AudioAdapter):
    def __init__(self) -> None:
        pass
    
    '''
    Generates a text from an audio_file
    '''
    async def generate_text_from_audio(self, file_path):
        client = Groq()
        with open(file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model="whisper-large-v3",
                prompt='''Give me what each person say based on the text you hear. Something like this:
                Doutor: Olá, tudo bem? O que te traz por cá?
                João: Olá Doutor, tenho tido tosse e febre
                ...
                ''', 
                response_format="json",
                language="pt",
                temperature=0.0
            )
            return transcription.text