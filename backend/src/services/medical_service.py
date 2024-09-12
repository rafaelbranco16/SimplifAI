from src import prompts
from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText
from src.services.entry_note_service import EntryNoteService
from src.loaders import loader
from src.services.llm_service import LLMService
from langchain_core.prompts import ChatPromptTemplate
from src import config
from src.domain.clinical_diary import ClinicalDiary
from src.adapters.clinical_diary_adapter import ClinicalDiaryAdapter

class MedicalService:
    def __init__(self) -> None:
        self.ai_service:LLMService = loader.loader.resolve(config.llm_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])
        self.clinical_diary_adapter:ClinicalDiaryAdapter = loader.loader.resolve(config.clinical_diary_adapter["name"])


    '''
    Summarizes the medical consultation
    @param text - the text to be summarized
    '''
    async def ai_summary(self, text:str, entry_note:EntryNote) -> MedicalConsultationText:
        medical_prompt = prompts.medical_consultation_prompt + str(entry_note.identification)
        messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
            ('system', medical_prompt),
            ('user', f'{text}')
        ])
        return MedicalConsultationText(await self.ai_service.send_messages(messages))
    
    async def create_clinical_diary(self, entry_note:EntryNote, mct:MedicalConsultationText) -> ClinicalDiary:
        return ClinicalDiary(entry_note, mct)
    
    async def save_clinical_diary(self, clinical_diary:ClinicalDiary):
        return await self.clinical_diary_adapter.save_clinical_diary(clinical_diary)