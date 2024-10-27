from src.logger import Logger
from src.loaders.load_database import load_database
from src.domain.discharge_note import DischargeNote

class DischargeNoteAdapter:
    def __init__(self)->None:
        self.db = load_database()
        self.db["DischargeNote"].create_index("id",unique=True,background=True)

    async def save_discharge_note(self, discharge_note:DischargeNote):
        try:
            Logger.print_info("Saving DischargeNote")
            discharge_note_dict = discharge_note.to_dict()
            self.db["DischargeNote"].insert_one(discharge_note_dict)
            return discharge_note
        except Exception as e:
                Logger.print_error(f"The following error occured: {str(e)}")
                raise RuntimeError("Something went wrong. Try again.")
    
    async def find_by_id(self, id) -> dict:
        return self.db["DischargeNote"].find_one({"id": id})