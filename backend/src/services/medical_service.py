from src import prompts
from src.domain.entry_note import EntryNote
from src.domain.medicalConsultationText import MedicalConsultationText
from src.loaders import loader
from src.services.llm_service import LLMService
from langchain_core.prompts import ChatPromptTemplate

class MedicalService:
    def __init__(self) -> None:
        pass

    '''
    Summarizes the medical consultation
    @param text - the text to be summarized
    '''
    async def ai_summary(text:str):
        ai_service:LLMService = loader.loader.resolve("LLMService")
        messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
            ('system', prompts.medical_consultation_prompt),
            ('user', '{text}')
        ])
        return await ai_service.send_messages(messages)