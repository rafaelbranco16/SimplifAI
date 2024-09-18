from src import config
from src.loaders import loader
from src.services.entry_note_service import EntryNoteService
from src.dto.entry_note_dto import EntryNoteDto
from src.logger import Logger
from fastapi.responses import JSONResponse
import traceback


class EntryNoteController:
    def __init__(self) -> None:
        self.service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])

    '''
    Creates an entry note
    @param entry_note_dto - The dto that contains the entry note information
    '''
    async def create_entry_note(self, entry_note_dto:EntryNoteDto):
        try:
            return {"message": await self.service.create_entry_note(entry_note_dto)}
        except Exception as e:
            error_message = traceback.format_exc()
            Logger.print_error(f"The following error occured: {str(e)}\n{error_message}")
            return JSONResponse(
                status_code=400,
                content={"message":"Something went wrong. Try again."}
            )
        
    async def get_entry_note(self, nif:str):
        try:
            return {"message": await self.service.find_entry_note_by_nif(nif)}
        except Exception as e:
            error_message = traceback.format_exc()
            Logger.print_error(f"The following error occured: {str(e)}\n{error_message}")
            return JSONResponse(
                status_code=400,
                content={"message":"Something went wrong. Try again."}
            )
