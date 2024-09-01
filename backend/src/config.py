import os
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv

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

llm_adapter = {
    "name":"GroqAdapter",
    "path":"src.adapters.groq_adapter"
}

gpt_model = "gpt-3.5-turbo"
groq_model = "llama-3.1-70b-versatile"

langfuse_host="https://cloud.langfuse.com"

langfuse_handler = CallbackHandler (
    secret_key=os.getenv("LANGFUSE_SK_KEY"),
    public_key=os.getenv("LANGFUSE_PB_KEY"),
    host=langfuse_host
)