from src import prompts
from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText
from src.services.entry_note_service import EntryNoteService
from src.loaders import loader
from src.services.llm_service import LLMService
from langchain_core.prompts import ChatPromptTemplate
from src import config
from src.domain.clinical_diary import ClinicalDiary
from src.domain.clinical_history import ClinicalHistory
from src.adapters.clinical_diary_adapter import ClinicalDiaryAdapter
from src.adapters.clinical_history_adapter import ClinicalHistoryAdapter

from src.mappers.medical_mapper import MedicalNoteMapper
from src.logger import Logger

class MedicalService:
    def __init__(self) -> None:
        self.ai_service:LLMService = loader.loader.resolve(config.llm_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])
        self.clinical_diary_adapter:ClinicalDiaryAdapter = loader.loader.resolve(config.clinical_diary_adapter["name"])
        self.clinical_history_adapter:ClinicalHistoryAdapter = loader.loader.resolve(config.clinical_history_adapter["name"])

    '''
    Summarizes the medical consultation
    @param text - the text to be summarized
    '''
    async def ai_summary(self, text:str, entry_note:EntryNote) -> MedicalConsultationText:
        try:
            medical_prompt = prompts.medical_consultation_prompt + str(entry_note.identification)
            messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
                ('system', medical_prompt),
                ('user', f'{text}')
            ])
            return MedicalConsultationText(await self.ai_service.send_messages(messages))
        except Exception as e:
            Logger.print_error(f"The following error occured: {str(e)}")
            raise ConnectionError("Something went wrong, try again.")
    
    async def create_clinical_diary(self, entry_note:EntryNote, mct:MedicalConsultationText) -> ClinicalDiary:
        return ClinicalDiary(entry_note, mct)
    
    async def save_clinical_diary(self, clinical_diary:ClinicalDiary):
        return await self.clinical_diary_adapter.save_clinical_diary(clinical_diary)
    
    async def find_clinical_diary_by_nif(self,nif:str):
        Logger.print_info(f"Searching for clinical diaries with NIF {nif}")
        result:list[dict] = await self.clinical_diary_adapter.find_by_nif(nif)
        c_diaries:list[ClinicalDiary] = []
        if result is None:
            Logger.print_warning(f"No clicial diaries found for this patient")
            raise ModuleNotFoundError("No clicial diaries found for this patient")
        for r in result:
            c_diaries.append(MedicalNoteMapper.to_obj(r))

        return c_diaries
    
    async def create_clinical_history(self, entry_note:EntryNote, mct:MedicalConsultationText) -> ClinicalHistory:
        return ClinicalHistory(entry_note, mct)

    async def save_clinical_history(self, clinical_history:ClinicalHistory):
        return await self.clinical_history_adapter.save_clinical_history(clinical_history)