from src.mappers.entry_note_mapper import EntryNoteMapper
from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText
from src.domain.clinical_diary import ClinicalDiary
from src.logger import Logger
import uuid

class MedicalNoteMapper:
    @staticmethod
    def to_dict(clinical_diary: ClinicalDiary) -> dict:
        """Converts a ClinicalDiary object to a dictionary."""
        return {
            "id": str(clinical_diary.id),
            "entry_note": clinical_diary.entry_note.to_dict(),
            "medical_consultation_text": clinical_diary.medical_consultation_text.to_dict()
        }

    @staticmethod
    def to_obj(clinical_diary_dict: dict) -> ClinicalDiary:
        """Converts a dictionary to a ClinicalDiary object."""
        entry_note = EntryNoteMapper.to_obj(clinical_diary_dict['entry_note'])
        Logger.print_info(clinical_diary_dict)
        medical_consultation_text = MedicalConsultationText(
            text=clinical_diary_dict['medical_consultation_text']
        )
        
        clinical_diary = ClinicalDiary(
            entry_note=entry_note,
            medical_consultation_text=medical_consultation_text
        )
        
        # Set the id if it exists, otherwise create a new UUID
        clinical_diary.id = uuid.UUID(clinical_diary_dict.get('id', str(uuid.uuid4())))
        
        return clinical_diary
