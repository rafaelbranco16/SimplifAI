from typing import TypedDict
from src.dto.identification_dto import IdentificationDto
from src.dto.usual_medication_dto import UsualMedicationDto
from src.dto.personal_background_dto import PersonalBackgroundDto
from src.dto.MCDT_dto import MCDTDto


class EntryNoteDto(TypedDict):
    allergies:list[str]
    identification:IdentificationDto
    usual_medication:list[UsualMedicationDto]
    personal_background:PersonalBackgroundDto
    actual_sickness_history:str
    mcdts:list[MCDTDto]

