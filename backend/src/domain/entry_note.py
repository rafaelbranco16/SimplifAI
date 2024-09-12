from src.domain.identification import Identification
from src.domain.usual_medication import UsualMedication
from src.domain.personal_background import PersonalBackground
import uuid

class EntryNote:
    def __init__(self, 
                 id:str|None, 
                 identification:Identification, 
                 allergies: list[str], 
                 usual_medication:list[UsualMedication], 
                 personal_background:PersonalBackground
    ):
        if id is None:
            self.id = uuid.uuid4()
            self.allergies = allergies
            self.identification = identification
            self.usual_medication = usual_medication
            self.personal_background = personal_background
        else:
            self.id = id
            self.allergies = allergies
            self.identification = identification
            self.usual_medication = usual_medication
            self.personal_background = personal_background
    '''
    Converts this object into a dict
    '''
    def to_dict(self):
        return {
            "id":str(self.id),
            "allergies": self.allergies,
            "identification": self.identification.to_dict(),
            "usual_medication": [med.to_dict() for med in self.usual_medication],
            "personal_background": self.personal_background.to_dict()
        }

