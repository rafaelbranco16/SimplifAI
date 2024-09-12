from typing import TypedDict

class ClinicalDiaryDto(TypedDict):
    pacient_name:str
    patient_gender:str
    patient_age:int
    cognitive_status:str
    functional_status:str
