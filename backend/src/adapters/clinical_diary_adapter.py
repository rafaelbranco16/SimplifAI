from src.loaders.load_database import load_database
from src.domain.clinical_diary import ClinicalDiary
from src.logger import Logger
class ClinicalDiaryAdapter:
    def __init__(self) -> None:
        self.db = load_database()
        self.db["ClinicalDiary"].create_index("id", unique=True, background=True)
    '''
    Saves a clinical diary

    @param clinical_diary - The clinical diary to be saved
    '''
    async def save_clinical_diary(self, clinical_diary:ClinicalDiary):
        try:
            Logger.print_info("Saving EntryNote...")
            clinical_diary_dict = clinical_diary.to_dict()
            self.db["ClinicalDiary"].insert_one(clinical_diary_dict)
            return clinical_diary
        except Exception as e:
            Logger.print_error(f"The following error occured: {str(e)}")
            raise RuntimeError("Something went wrong. Try again.")
    
    '''
    Checks if a certain clinical diary exists by its id

    @param id - The id of the clinical diary
    '''
    async def exists(self, id:str):
        return self.db["ClinicalDiary"].find_one({"id":id})
    
    async def find_by_nif(self, nif: str)->dict:
        Logger.print_info(f"Type of collection: {type(self.db['ClinicalDiary'])}")
        return self.db["ClinicalDiary"].find_one({"entry_note.identification.nif":nif})
