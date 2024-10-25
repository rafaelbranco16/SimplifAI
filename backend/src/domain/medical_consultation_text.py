from src.logger import Logger

class MedicalConsultationText:
    def __init__(self, text: str):
        self.text = text
        Logger.print_info("Created a new medical consultation text")

    def __str__(self):
        return self.text
    
    '''
    Validates the parameters
    @param entry_note - The entry note that has the user identification
    @param text - The text with the medical consultation
    '''
    def validations(text:str):
        if(text is None or text == ""):
            raise ValueError("The medical consultation text is invalid text is invalid")
        
    def to_dict(self):
        return self.text