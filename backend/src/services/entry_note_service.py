from src.dto.entry_note_dto import EntryNoteDto
from src.domain.entry_note import EntryNote
from src.adapters.entry_note_adapter import EntryNoteAdapter
from src.domain.usual_medication import UsualMedication
from src.domain.personal_background import PersonalBackground
from src.domain.identification import Identification
from src.logger import Logger
from src.loaders import loader
from src import config

class EntryNoteService:
    def __init__(self) -> None:
        self.entry_note_adapter:EntryNoteAdapter = loader.loader.resolve(config.entry_note_adapter["name"])

    '''
    Creates an entry note
    '''
    async def create_entry_note(self, entry_note_dto:EntryNoteDto):
        identification:Identification = Identification(
            entry_note_dto["identification"]["name"],
            entry_note_dto["identification"]["gender"],
            entry_note_dto["identification"]["age"],
            entry_note_dto["identification"]["cognitive_status"],
            entry_note_dto["identification"]["functional_status"]
        )

        usual_medication_list:list[UsualMedication] = []
        for usual_medication in entry_note_dto["usual_medication"]:
            um:UsualMedication = UsualMedication(usual_medication["medication"], usual_medication["dose"])
            usual_medication_list.append(um)
        
        personal_background:PersonalBackground = PersonalBackground(
            entry_note_dto["personal_background"]["medical_background"],
            entry_note_dto["personal_background"]["cirurgic_background"]
        )

        entry_note:EntryNote = EntryNote(
            identification, 
            entry_note_dto["allergies"], 
            usual_medication_list, 
            personal_background
        )
        entry_note.identification
        saved_entry_note = await self.entry_note_adapter.save_entry_note(entry_note)

        return {"message":saved_entry_note}
        
