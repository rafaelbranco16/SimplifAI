from src.domain.entry_note import EntryNote

class MedicalConsultationText:
    def __init__(self, text: str):
        self.validations(text)

    def __str__(self):
        return f"MedicalConsultationText(Text: {self.text})"
    
    '''
    Validates the parameters
    @param entry_note - The entry note that has the user identification
    @param text - The text with the medical consultation
    '''
    def validations(text:str):
        if(text is None or text is ""):
            raise ValueError("The text is invalid")