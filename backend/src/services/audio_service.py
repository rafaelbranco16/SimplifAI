'''
This service will only transcribe audio into text
'''
from src.loaders import loader
from src import config
from src.adapters.audio_adapter import AudioAdapter
from src.adapters.llm_adapter import LLMAdapter
from fastapi import UploadFile
from langchain_core.prompts import ChatPromptTemplate
import os
import json

class AudioService:
    def __init__(self) -> None:
        self.audio_adapter:AudioAdapter = loader.loader.resolve(config.audio_adapter["name"])
        self.llm_adapter:LLMAdapter = loader.loader.resolve(config.llm_adapter["name"])

    async def generate_text_from_audio(self, file):
         # Step 1: Save the uploaded file locally
        file_path = await self.save_file(file)

        # Step 2: Call the WhisperAdapter to transcribe the audio
        transcription = await self.audio_adapter.generate_text_from_audio(file_path)
        messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
                ('system', '''You are pro into defining what each person is saying on a certain text in a medical consultation.
For example, for the given text:
Olá,João, tudo bem, sou o Dr. Cornélio, o que o traz aqui? Olá, Doutor, sofro bastante do estômago. Ora bem, isso parece-me ser uma gastroentrite! Toma isto para acalmar!
Returns:
Doctor:Olá,João, tudo bem, sou o Dr. Cornélio, o que o traz aqui?
João: Olá, Doutor, sofro bastante do estômago.
Doctor:Ora bem, isso parece-me ser uma gastroentrite! Toma isto para acalmar!
Before each person add a line break and dont make any coment about the given text
                 '''),
                ('user', f'{transcription}')
            ])
        

        return await self.llm_adapter.send_messages(messages)

    async def save_file(self, file: UploadFile) -> str:
        # Ensure that the "temp" directory exists
        os.makedirs("temp", exist_ok=True)
        
        # Define the path where the file will be saved
        file_location = os.path.join("temp", file.filename)        
        # Save the file
        with open(file_location, "wb") as f:
            f.write(await file.read())

        return file_location
    
    async def generate_entry_note_from_audio(self, file):
        messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
                ('system', '''You are an expert in creating structured JSON data from simple text. Based on the information I give you, respond only with JSON that follows this exact structure, using placeholders where needed:

{{
  "allergies": ["{{allergies}}"],
  "identification": {{
    "name": "{{name}}",
    "gender": "{{gender}}",
    "age": {{int of the age}},
    "cognitive_status": "{{cognitive_status}}",
    "functional_status": "{{functional_status}}",
    "nif": "{{nif}}"
  }},
  "usual_medication": [
    {{
      "medication": "{{medication}}",
      "dose": "{{dose}}"
    }}
  ],
  "personal_background": {{
    "medical_background": "{{medical_background}}",
    "cirurgic_background": "{{cirurgic_background}}"
  }}
}}

Only use information explicitly provided in the text, leaving placeholders if no information is available for a field. Replace the example values only when relevant data is provided. Return only a valid JSON object based on the information I provide.
                 ''')
,
                ('user', f'{file}')
            ])
        
        return await self.llm_adapter.send_messages(messages)