from src.dto.entry_note_dto import EntryNoteDto
from src.domain.entry_note import EntryNote
from src.adapters.entry_note_adapter import EntryNoteAdapter
from src.domain.usual_medication import UsualMedication
from src.domain.MCDT import MCDT

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
        mcdts:list[UsualMedication] = []
        for mcdt in entry_note_dto["mcdts"]:
            um:MCDT = MCDT(mcdt["type"], mcdt["text"])
            mcdts.append(um)
        if entry_note_dto == None or entry_note_dto["actual_sickness_history"] == "":
            raise NameError("The actual_sickness_history is invalid")
        ash = entry_note_dto["actual_sickness_history"]
        entry_note:EntryNote = EntryNote(
            None,
            identification,
            entry_note_dto["allergies"],
            usual_medication_list,
            personal_background,
            ash,
            mcdts
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
    
    async def find_entry_note_by_nif(self, nif:str):
        result:dict = await self.entry_note_adapter.find_by_nif(nif)
        if result is None:
            Logger.print_warning(f"The entry note with the id {id} does NOT exist.")
            raise ModuleNotFoundError("This entry note does not exist.")
        return EntryNoteMapper.to_obj(result)


    def format_entry_note(self, entry_note: EntryNote) -> str:
        # Format identification
        identification = entry_note.identification
        formatted_identification = (
            f"Name: {identification.name}\n"
            f"Gender: {identification.gender}\n"
            f"Age: {identification.age}\n"
            f"Cognitive Status: {identification.cognitive_status}\n"
            f"Functional Status: {identification.functional_status}\n"
            f"NIF: {identification.nif}\n"
            f"Actual Sickness: {entry_note.actual_sickness_history}\n"  
        )

        # Format allergies
        formatted_allergies = f"Allergies: {', '.join(entry_note.allergies) if entry_note.allergies else 'None'}\n"

        # Format usual medications
        formatted_medications = "Usual Medications:\n"
        if entry_note.usual_medication:
            for medication in entry_note.usual_medication:
                formatted_medications += f"- Medication: {medication.medication}, Dose: {medication.dose}\n"
        else:
            formatted_medications += "None\n"

        # Format usual medications
        formatted_mcdts = "MCDTSs:\n"
        if entry_note.mcdts:
            for mcdt in entry_note.mcdts:
                formatted_mcdts += f"- MCDT: {mcdt.type}, Description: {mcdt.text}\n"
        else:
            formatted_mcdts += "Nenhuma\n"
        # Format personal background
        personal_background = entry_note.personal_background
        formatted_background = (
            f"Medical Background: {personal_background.medical_background}\n"
            f"Surgical Background: {personal_background.cirurgic_background}\n"
        )

        # Combine everything into the final string
        formatted_entry_note = (
            f"Identification:\n{formatted_identification}\n"
            f"{formatted_allergies}\n"
            f"{formatted_medications}\n"
            f"Personal Background:\n{formatted_background}"
            f"MCDTs:\n{formatted_mcdts}"
        )

        return formatted_entry_note