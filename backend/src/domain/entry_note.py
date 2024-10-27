from src.domain.identification import Identification
from src.domain.usual_medication import UsualMedication
from src.domain.personal_background import PersonalBackground
from src.domain.MCDT import MCDT

import uuid

class EntryNote:
    def __init__(self, 
                 id:str|None, 
                 identification:Identification, 
                 allergies: list[str], 
                 usual_medication:list[UsualMedication], 
                 personal_background:PersonalBackground,
                 actual_sickness_history:str,
                 mcdts:list[MCDT]
    ):
        if id is None:
            self.id = uuid.uuid4()
            self.allergies = allergies
            self.identification = identification
            self.usual_medication = usual_medication
            self.personal_background = personal_background
            self.actual_sickness_history = actual_sickness_history
            self.mcdts = mcdts
        else:
            self.id = id
            self.allergies = allergies
            self.identification = identification
            self.usual_medication = usual_medication
            self.personal_background = personal_background
            self.actual_sickness_history = actual_sickness_history
            self.mcdts = mcdts
    '''
    Converts this object into a dict
    '''
    def to_dict(self):
        return {
            "id":str(self.id),
            "allergies": self.allergies,
            "identification": self.identification.to_dict(),
            "usual_medication": [med.to_dict() for med in self.usual_medication],
            "personal_background": self.personal_background.to_dict(),
            "actual_sickness_history":self.actual_sickness_history,
            "mcdts":[mcdt.to_dict() for mcdt in self.mcdts]
        }

