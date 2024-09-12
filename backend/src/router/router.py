from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.document_controller import DocumentController
from src.controllers.llm_controller import LLMController
from src.controllers.entry_note_controller import EntryNoteController
from src.controllers.medical_controller import MedicalController
from src import config
from src.dto.request_dto import RequestDto
from src.dto.entry_note_dto import EntryNoteDto
from src.logger import Logger
from fastapi import Body

router = APIRouter()

class Router:
    @router.get("/")
    async def default():
        document_loader_controller:DocumentController = loader.resolve(config.controllers["document_controller"]) 
        return await document_loader_controller.default()
    @router.post("/prompt/")
    async def send_prompt(request_dto:RequestDto):
        llm_controller:LLMController = loader.resolve(config.llm_controller["name"])
        return await llm_controller.send_prompt(request_dto)
    '''
    Creates a new entry note using a DTO
    '''
    @router.post("/entry-note/")
    async def create_entry_note(entry_note_dto:EntryNoteDto):
        entry_note_controller:EntryNoteController = loader.resolve(config.entry_note_controller["name"])
        return await entry_note_controller.create_entry_note(entry_note_dto)
    
    @router.post("/clinical-diary/")
    async def create_clinical_diary(id: str = Body(...), mct: str = Body(...)):
        ctrl: MedicalController = loader.resolve(config.medical_controller["name"])
        return await ctrl.create_clinical_diary(id, mct)