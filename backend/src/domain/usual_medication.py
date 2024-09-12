from src.logger import Logger
class UsualMedication:
    '''
    Constructor

    @param medication - a list with the 
    '''
    def __init__(self, medication: str, dose: str):
        self.medication = medication
        self.dose = dose
        Logger.print_info("Created a new medication")

    def to_dict(self):
        return {
            "medication": self.medication,
            "dose": self.dose
        }


    