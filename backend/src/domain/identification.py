from src.logger import Logger
class Identification:
    '''
    @param name - The name of the patient
    @param gender - The gender of the patient
    @param age - The age of the patient
    @param cognitive_status - The congitive status of the patient
    @param function_status- The functional status of the patient
    '''
    def __init__(self, name:str, gender: str, age: int, cognitive_status: str, function_status: str, nif:str):
        self.name = name
        self.gender = gender
        self.age = age
        self.cognitive_status = cognitive_status
        self.function_status = function_status
        self.nif = nif
        Logger.print_info(f"Created a new identification with the name: {self.name}")

    '''
    A default string for this class
    '''
    def __str__(self):
        return (f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}, "
                f"Cognitive Status: {self.cognitive_status}, Function Status: {self.function_status})")
    
    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "cognitive_status": self.cognitive_status,
            "function_status": self.function_status,
            "nif":self.nif
        }

