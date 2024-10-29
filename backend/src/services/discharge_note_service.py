from src.services.entry_note_service import EntryNoteService
from src.logger import Logger
from typing import List
from src.services.llm_service import LLMService
from src import prompts

from src.adapters.discharge_note_adapter import DischargeNoteAdapter
from src.domain.clinical_diary import ClinicalDiary
from src.domain.discharge_text import DischargeText
from src.domain.discharge_note import DischargeNote
from src.dto.discharge_note_dto import DischargeNoteDto
from src.domain.entry_note import EntryNote
from langchain_core.prompts import ChatPromptTemplate

from src.loaders import loader
from src import config
class DischargeNoteService :
    def __init__(self) -> None:
        self.discharge_note_adapter: DischargeNoteAdapter = loader.loader.resolve(config.discharge_note_adapter["name"])
        self.ai_service:LLMService = loader.loader.resolve(config.llm_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])

        
    async def generated_discharge(self, entry_note: EntryNote, clinical_diaries: List[ClinicalDiary]) -> DischargeText:
        try:
            prompt = prompts.discharge_note_prompt
            prompt = prompt.replace("[Insert the entry note exactly as you did above]", self.entry_note_service.format_entry_note(entry_note))
            prompt = prompt.replace("[Insert all the clinical diaries as you did above]", self.format_clinical_diaries(clinical_diaries))
            messages:ChatPromptTemplate = ChatPromptTemplate.from_messages([
                ('system', prompt),
            ])
            return DischargeText(await self.ai_service.send_messages(messages))
        except Exception as e:
            Logger.print_error(f"The following error occurred: {str(e)}")
            raise ConnectionError("Something went wrong")
                               
        

    #formatar clinical diaries numa string
    def format_clinical_diaries(self, clinical_diaries: List[ClinicalDiary]) -> str:
        formatted_diaries = ""
        for diary in clinical_diaries:
            formatted_diaries += f"Entry: {diary.medical_consultation_text.text}\n"
        return formatted_diaries


    async def create_discharge_note(self, entry_note: EntryNote, discharge_text: DischargeText) -> DischargeNote:
        return DischargeNote(entry_note, discharge_text.text)

    '''
    Saves the discharge note using the DischargeNoteAdapter.
    @param discharge_note - The discharge note to be saved.
    '''
    async def save_discharge_note(self, discharge_note_dto: DischargeNoteDto):
        Logger.print_info(discharge_note_dto)
        entry_note:EntryNote = await self.entry_note_service.create_entry_note(discharge_note_dto["entry_note"])
        discharge_note:DischargeNote = await self.create_discharge_note(entry_note, DischargeText(discharge_note_dto["discharge_text"]["text"]))
        await self.discharge_note_adapter.save_discharge_note(discharge_note)
        return discharge_note
