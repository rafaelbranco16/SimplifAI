from src import config
from src.loaders import loader
from src.services.entry_note_service import EntryNoteService
from src.dto.entry_note_dto import EntryNoteDto


class EntryNoteController:
    def __init__(self) -> None:
        self.service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])

    '''
    Creates an entry note
    @param entry_note_dto - The dto that contains the entry note information
    '''
    async def create_entry_note(self, entry_note_dto:EntryNoteDto):
        return await self.service.create_entry_note(entry_note_dto)