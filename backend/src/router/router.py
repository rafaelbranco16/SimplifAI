from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.document_controller import DocumentController
from src.controllers.llm_controller import LLMController
from src.controllers.entry_note_controller import EntryNoteController
from src import config
from src.dto.request_dto import RequestDto
from src.dto.entry_note_dto import EntryNoteDto
from src.logger import Logger

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
    async def create_clinical_diary(entry_note_dto:EntryNoteDto):
        entry_note_controller:EntryNoteController = loader.resolve(config.entry_note_controller["name"])
        return await entry_note_controller.create_entry_note(entry_note_dto)