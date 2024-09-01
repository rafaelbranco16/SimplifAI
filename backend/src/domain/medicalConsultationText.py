from src.domain.entryNote import EntryNote

class MedicalConsultationText:
    def __init__(self, entry_note:EntryNote, text: str):
        self.validations(entry_note, text)
        self.text = text
        self.entry_note = entry_note

    def __str__(self):
        return f"MedicalConsultationText(Text: {self.text})"
    
    '''
    Validates the parameters
    @param entry_note - The entry note that has the user identification
    @param text - The text with the medical consultation
    '''
    def validations(entry_note:EntryNote, text:str):
        if(entry_note is None):
            raise ValueError("The entry note should not be null")
        if(text is None or text is ""):
            raise ValueError("The text is invalid")