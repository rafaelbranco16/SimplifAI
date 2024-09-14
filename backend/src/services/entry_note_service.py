from src.dto.entry_note_dto import EntryNoteDto
from src.domain.entry_note import EntryNote
from src.adapters.entry_note_adapter import EntryNoteAdapter
from src.domain.usual_medication import UsualMedication
from src.domain.personal_background import PersonalBackground
from src.domain.identification import Identification
from src.logger import Logger
from src.loaders import loader
from src import config
from src.mappers.entry_note_mapper import EntryNoteMapper

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
            entry_note_dto["identification"]["functional_status"],
            entry_note_dto["identification"]["nif"]
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
            None,
            identification,
            entry_note_dto["allergies"],
            usual_medication_list,
            personal_background
        )
        return await self.entry_note_adapter.save_entry_note(entry_note)
    
    '''
    Searches for a entry note by its id
    @param id - The id of the entry note
    '''
    async def find_entry_note_by_id(self, id:str):
        result:dict = await self.entry_note_adapter.find_by_id(id)
        if result is None:
            Logger.print_warning(f"The entry note with the id {id} does NOT exist.")
            raise ModuleNotFoundError("This entry note does not exist.")
        return EntryNoteMapper.to_obj(result)
        
