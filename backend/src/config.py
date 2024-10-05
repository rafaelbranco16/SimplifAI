import os
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

llm_controller = {
    "name":"LLMController",
    "path":"src.controllers.llm_controller"
}
medical_controller = {
    "name":"MedicalController",
    "path":"src.controllers.medical_controller"
}

document_controller = {
    "name":"DocumentController",
    "path":"src.controllers.document_controller"
}

entry_note_controller = {
    "name":"EntryNoteController",
    "path":"src.controllers.entry_note_controller"
}

audio_controller = {
    "name":"AudioController",
    "path":"src.controllers.audio_controller"
}

discharge_note_controller = {
    "name":"DischargeNoteController",
    "path":"src.controllers.discharge_note_controller"
}

document_service = {
    "name":"DocumentService",
    "path":"src.services.document_service"
}

llm_service = {
    "name":"LLMService",
    "path":"src.services.llm_service"
}

medical_service = {
    "name":"MedicalService",
    "path":"src.services.medical_service"
}

entry_note_service = {
    "name":"EntryNoteService",
    "path":"src.services.entry_note_service"
}

audio_service = {
    "name":"AudioService",
    "path":"src.services.audio_service"
}

discharge_note_service = {
    "name":"DischargeNoteService",
    "path":"src.services.discharge_note_service"
}

llm_adapter = {
    "name":"GroqAdapter",
    "path":"src.adapters.groq_adapter"
}

entry_note_adapter = {
    "name":"EntryNoteAdapter",
    "path":"src.adapters.entry_note_adapter"
}

clinical_diary_adapter = {
    "name":"ClinicalDiaryAdapter",
    "path":"src.adapters.clinical_diary_adapter"
}

audio_adapter = {
    "name":"WhisperAdapter",
    "path":"src.adapters.whisper_adapter"
}

discharge_note_adapter = {
    "name":"DischargeNoteAdapter",
    "path":"src.adapters.discharge_note_adapter"
}


gpt_model = "gpt-3.5-turbo"
groq_model = "llama-3.1-70b-versatile"

langfuse_host="https://cloud.langfuse.com"

langfuse_handler = CallbackHandler (
    secret_key=os.getenv("LANGFUSE_SK_KEY"),
    public_key=os.getenv("LANGFUSE_PB_KEY"),
    host=langfuse_host
)

db_connection_string=os.getenv("DB_CONNECTION_STRING")
client = MongoClient(db_connection_string)
client_db_name = "SimplifAI"