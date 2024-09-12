from src.logger import Logger
class PersonalBackground:
    '''
    Constructor

    @param medical_background - The medical background of the patient
    @param cirurgic_background - The cirurgic background of the patient
    '''
    def __init__(self, medical_background: str, cirurgic_background: str):
        self.medical_background = medical_background
        self.cirurgic_background = cirurgic_background
        Logger.print_info(f"Created a new personal background: {self}")

    def __str__(self):
        return str(self.__dict__)
    
    def to_dict(self):
        return {
            "medical_background": self.medical_background,
            "cirurgic_background": self.cirurgic_background
        }


