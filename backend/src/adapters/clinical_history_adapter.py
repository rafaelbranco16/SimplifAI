from src.loaders.load_database import load_database
from src.domain.clinical_history import ClinicalHistory
from src.logger import Logger
class ClinicalHistoryAdapter:
    def __init__(self) -> None:
        self.db = load_database()
        self.db["ClinicalHistory"].create_index("id", unique=True, background=True)
    '''
    Saves a clinical clinical history

    @param clinical_diary - The clinical history to be saved
    '''
    async def save_clinical_history(self, clinical_history:ClinicalHistory):
        Logger.print_info(clinical_history)
        try:
            Logger.print_info("Saving EntryNote...")
            clinical_history_dict = clinical_history.to_dict()
            self.db["ClinicalHistory"].insert_one(clinical_history_dict)
            return clinical_history
        except Exception as e:
            Logger.print_error(f"The following error occured: {str(e)}")
            raise RuntimeError("Something went wrong. Try again.")
    
    '''
    Checks if a certain clinical diary exists by its id

    @param id - The id of the clinical diary
    '''
    async def exists(self, id:str):
        return self.db["ClinicalHistory"].find_one({"id":id})
    
    async def find_by_nif(self, nif: str)->dict:
        cursor = self.db["ClinicalHistory"].find({"entry_note.identification.nif": nif})
    
        result = []
        for document in cursor:
            result.append(document)

        return result
