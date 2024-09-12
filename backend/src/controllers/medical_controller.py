from src import config

from src.loaders import loader

from src.dto.entry_note_dto import EntryNoteDto

from src.domain.entry_note import EntryNote
from src.domain.medical_consultation_text import MedicalConsultationText

from src.services.entry_note_service import EntryNoteService
from src.services.medical_service import MedicalService

from fastapi.responses import JSONResponse

from src.logger import Logger

class MedicalController:
    def __init__(self) -> None:
        self.service:MedicalService = loader.loader.resolve(config.medical_service["name"])
        self.entry_note_service:EntryNoteService = loader.loader.resolve(config.entry_note_service["name"])

    '''
    Creates a clinical diary

    @param id - The id of the clinical diary
    @param medical_consultation_text - The audio of the medical consultation converted into text
    '''
    async def create_clinical_diary(self, id:str, medical_consultation_text:str):
        try:
            entry_note:EntryNote = await self.entry_note_service.find_entry_note_by_id(id)
            ai_text:MedicalConsultationText = await self.service.ai_summary(medical_consultation_text, entry_note)
            clinical_diary = await self.service.create_clinical_diary(entry_note, ai_text)
            saved_diary = await self.service.save_clinical_diary(clinical_diary)

            return {"message": saved_diary}
        except ModuleNotFoundError as not_found:
            Logger.print_error(str(not_found))
            return JSONResponse(
                status_code=404,
                content={"message":str(not_found)}
            )
        except Exception as e:
            Logger.print_error(str(e))
            return JSONResponse(
                status_code=400,
                content={"message":str(e)}
            )
        



