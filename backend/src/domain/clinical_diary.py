from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText
import uuid

class ClinicalDiary:
    def __init__(self, entry_note:EntryNote, medical_consultation_text:MedicalConsultationText):
        self.id = uuid.uuid4()
        self.entry_note:EntryNote = entry_note
        self.medical_consultation_text:MedicalConsultationText = medical_consultation_text

    def to_dict(self):
        return {
            "id": str(self.id),
            "enytr_note": self.entry_note.to_dict(),
            "medical_consultation_text": self.medical_consultation_text.to_dict()
        }

