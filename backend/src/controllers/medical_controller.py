from src.loaders import loader
from src import config
from src.services.entry_note_service import EntryNoteService
from src.dto.entry_note_dto import EntryNoteDto
from src.domain.entry_note import EntryNote
from src.services.medical_service import MedicalService
from src.domain.medical_consultation_text import MedicalConsultationText

class MedicalController:
    def __init__(self) -> None:
        self.service:MedicalService = loader.loader.resolve(config.medical_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])

    async def create_clinical_diary(self, id:str, medical_consultation_text:str):
        entry_note:EntryNote = await self.entry_note_service.find_entry_note_by_id(id)
        ai_text:MedicalConsultationText = await self.service.ai_summary(medical_consultation_text, entry_note)
        clinical_diary = await self.service.create_clinical_diary(entry_note, ai_text)
        saved_diary = await self.service.save_clinical_diary(clinical_diary)

        return saved_diary
        



