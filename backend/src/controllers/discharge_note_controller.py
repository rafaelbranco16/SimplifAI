from typing import List
from src.domain.clinical_diary import ClinicalDiary
from src.services.medical_service import MedicalService
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
        self.clinical_diary_service:MedicalService = loader.loader.resolve(config.medical_service["name"])

    async def create_discharge_note(self,nif:str):
        try:
            # obter entry note com nif
            entry_note:EntryNote = await self.entry_note_service.find_entry_note_by_nif(nif)

            Logger.print_info("controller 1")

            #obter clinical diaries com nif
            clinical_diaries: List[ClinicalDiary] = await self.clinical_diary_service.find_clinical_diary_by_nif(nif)

            Logger.print_info("controller 2")


            ai_text = await self.service.generated_discharge(entry_note, clinical_diaries)
            discharge_note = await self.service.create_discharge_note(entry_note, ai_text)
            await self.service.save_discharge_note(discharge_note)

            return {'message': discharge_note}
        except ModuleNotFoundError as not_found:
                Logger.print_error(str(not_found))  
                return JSONResponse(
                    status_code=404,
                    content={"message": str(not_found)}
                )
            

