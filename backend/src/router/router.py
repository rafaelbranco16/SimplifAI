from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.document_controller import DocumentController
from src.controllers.llm_controller import LLMController
from src import config
from src.dto.request_dto import RequestDto

router = APIRouter()

class Router:
    @router.get("/")
    async def default():
        document_loader_controller:DocumentController = loader.resolve(config.controllers["document_controller"]) 
        return await document_loader_controller.default()
    @router.post("/prompt/")
    async def send_prompt(request_dto:RequestDto):
        llm_controller:LLMController = loader.resolve(config.controllers.get("llm_controller").get("name"))
        return await llm_controller.send_prompt(request_dto)