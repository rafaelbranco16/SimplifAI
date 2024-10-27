from src.logger import Logger
class MCDT:
    '''
    Constructor

    @param medication - the name of the type
    @param text - the dosation of the refered text
    '''
    def __init__(self, type: str, text: str):
        self.type = type
        self.text = text
        Logger.print_info("Created a new medication")

    '''
    Validates all the parameters from the class
    '''
    def validation(self, type:str, text:str):
        if type is None or type == "":
            raise ValueError("This type is invalid.")
        if text is None or text == "":
            raise ValueError(f"The text is invalid.")
    
    '''
    Converts this object into a dict
    '''
    def to_dict(self):
        return {
            "type": self.type,
            "text": self.text
        }


    