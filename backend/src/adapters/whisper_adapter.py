from src.adapters.audio_adapter import AudioAdapter
from groq import Groq
import whisper

class WhisperAdapter(AudioAdapter):
    def __init__(self) -> None:
        pass
    
    '''
    Generates a text from an audio_file
    '''
    async def generate_text_from_audio(self, file_path):
        model = whisper.load_model("large-v3")
        result = model.transcribe(file_path)
        return result["text"]