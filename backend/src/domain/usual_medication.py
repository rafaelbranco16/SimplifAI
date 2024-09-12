from src.logger import Logger
class UsualMedication:
    '''
    Constructor

    @param medication - the name of the medication
    @param dose - the dosation of the refered medication
    '''
    def __init__(self, medication: str, dose: str):
        self.medication = medication
        self.dose = dose
        Logger.print_info("Created a new medication")

    '''
    Validates all the parameters from the class
    '''
    def validation(self, medication:str, dose:str):
        if medication is None or medication == "":
            raise ValueError("This medication is invalid.")
        if dose is None or dose == "":
            raise ValueError(f"The dosation for the medication {medication} is invalid.")
    
    '''
    Converts this object into a dict
    '''
    def to_dict(self):
        return {
            "medication": self.medication,
            "dose": self.dose
        }


    