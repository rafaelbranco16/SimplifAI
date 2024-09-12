from src.loaders.load_database import load_database
from src.domain.clinical_diary import ClinicalDiary
from src.logger import Logger
class ClinicalDiaryAdapter:
    def __init__(self) -> None:
        self.db = load_database()

    async def save_clinical_diary(self, clinical_diary:ClinicalDiary):
        Logger.print_info("Saving EntryNote...")
        clinical_diary_dict = clinical_diary.to_dict()
        self.db["ClinicalDiary"].insert_one(clinical_diary_dict)
        return clinical_diary
    
    async def exists(self, id):
        return self.db["ClinicalDiary"].find_one({"id":id})
