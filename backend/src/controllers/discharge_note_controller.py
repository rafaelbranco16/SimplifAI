from src.domain.entry_note import EntryNote
from src.services.discharge_note_service import DischargeNoteService
from src.services.entry_note_service import EntryNoteService
from src import config
from src.loaders import loader
from src.logger import Logger
from fastapi.responses import JSONResponse

from src.services.entry_note_service import EntryNoteService


class DischargeNoteController:
    def __init__(self) -> None:
        self.service:DischargeNoteService = loader.loader.resolve(config.discharge_note_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])
        self.clinical_diary_service = loader.loader.resolve(config.medical_service["name"])



async def create_discharge_note(self,nif:str):
    try:
        entry_note:EntryNote = await self.entry_note_service.find_entry_note_by_nif(nif)
        clinical_diaries = await self.clinical_diary_service.find_by_nif(nif)
        ai_text = await self.service.generated_discharge(entry_note, clinical_diaries)
        discharge_note = await self.service.create_discharge_note(entry_note, ai_text)

        return {'message': discharge_note}
    except ModuleNotFoundError as not_found:
            Logger.print_error(str(not_found))
            return JSONResponse(
                status_code=404,
                content={"message":str(not_found)}
            )
        

