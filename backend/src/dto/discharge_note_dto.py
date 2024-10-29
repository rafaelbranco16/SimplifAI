from typing import TypedDict
from src.dto.entry_note_dto import EntryNoteDto
from src.dto.discharge_text_dto import DischargeTextDto


class DischargeNoteDto(TypedDict):
    entry_note:EntryNoteDto
    discharge_text:DischargeTextDto
