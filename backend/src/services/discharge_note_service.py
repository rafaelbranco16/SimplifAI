from typing import List
from src import prompts

from src.adapters.discharge_note_adapter import DischargeNoteAdapter
from src.domain.clinical_diary import ClinicalDiary
from src.domain.discharge_text import DischargeText
from src.domain.discharge_note import DischargeNote
from src.domain.entry_note import EntryNote
from src.loaders import loader
from src import config
class DischargeNoteService :
    def __init__(self) -> None:
        self.discharge_note_adapter: DischargeNoteAdapter = loader.loader.resolve(config.discharge_note_adapter["name"])

        '''
        async def ai_summary(self, entry_note: EntryNote, clinical_diaries: List[ClinicalDiary]) -> DischargeText:
        try:
            # Build the AI prompt using the discharge_note_prompt template
            prompt = prompts.discharge_note_prompt
            prompt = prompt.replace("[Insert the entry note exactly as you did above]", self.format_entry_note(entry_note))
            prompt = prompt.replace("[Insert all the clinical diaries as you did above]", self.format_clinical_diaries(clinical_diaries))
        '''

 #formatar clinical diaries numa string
    def format_clinical_diaries(self, clinical_diaries: List[ClinicalDiary]) -> str:
        formatted_diaries = ""
        for diary in clinical_diaries:
            formatted_diaries += f"Date: {diary.date}\nEntry: {diary.entry_text}\n"
        return formatted_diaries


    async def create_discharge_note(self, entry_note: EntryNote, discharge_text: DischargeText) -> DischargeNote:
        return DischargeNote(entry_note, discharge_text.text)

    '''
    Saves the discharge note using the DischargeNoteAdapter.
    @param discharge_note - The discharge note to be saved.
    '''
    async def save_discharge_note(self, discharge_note: DischargeNote):
        return await self.discharge_note_adapter.save_discharge_note(discharge_note)
