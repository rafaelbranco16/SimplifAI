from src.loaders.load_database import load_database
from src.domain.entry_note import EntryNote
from src.logger import Logger
import pickle as pkl

class EntryNoteAdapter:
    def __init__(self) -> None:
        self.db = load_database()

    async def save_entry_note(self, entry_note:EntryNote):
        Logger.print_info("Saving EntryNote...")
        entry_note_dict = entry_note.to_dict()
        self.db["EntryNote"].insert_one(entry_note_dict)
        return entry_note
    
    async def find_by_id(self, id) -> dict:
        return self.db["EntryNote"].find_one({"id":id})
