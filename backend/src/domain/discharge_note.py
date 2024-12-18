import uuid
from src.domain.discharge_text import DischargeText
from src.domain.entry_note import EntryNote
from src.domain.clinical_diary import ClinicalDiary

class DischargeNote:
    def __init__(self, entry_note: EntryNote, discharge_text: str):
        self.id = uuid.uuid4()
        self.entry_note:EntryNote= entry_note
        self.discharge_text:DischargeText= discharge_text
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "entry_note": self.entry_note.to_dict(),  
            "discharge_text": self.discharge_text
        }

    def __str__(self):
        return f"DischargeNote(ID: {self.id}, EntryNote: {self.entry_note}, Discharge Text: {self.discharge_text})"
