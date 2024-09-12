from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText
from src.logger import Logger
import uuid

class ClinicalDiary:
    def __init__(self, entry_note:EntryNote, medical_consultation_text:MedicalConsultationText):
        self.validation(entry_note, medical_consultation_text)
        self.id = uuid.uuid4()
        self.entry_note:EntryNote = entry_note
        self.medical_consultation_text:MedicalConsultationText = medical_consultation_text
    '''
    Validates if the variables to create the clinical diary are valid

    @param entry_note - The entry note
    @param medical_consultation_text - The medical consultation text
    '''
    def validation(self, entry_note, medical_consultation_text):
        if entry_note is None:
            Logger.print_error("The entry note to create the clinical diary was None")
            raise ValueError("Something went wrong. Try again.")
        if medical_consultation_text is None:
            Logger.print_error("The medical consultation text to create the clinical diary was None")
            raise ValueError("Something went wrong. Try again.")
    
    '''
    Converts this object into a dict
    '''
    def to_dict(self):
        return {
            "id": str(self.id),
            "enytr_note": self.entry_note.to_dict(),
            "medical_consultation_text": self.medical_consultation_text.to_dict()
        }

