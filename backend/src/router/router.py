from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.document_controller import DocumentController
from src.controllers.llm_controller import LLMController
from src import config

router = APIRouter()

class Router:
    @router.get("/")
    async def default():
        document_loader_controller:DocumentController = loader.resolve(config.controllers["document_controller"]) 
        return await document_loader_controller.default()
    @router.get("/prompt")
    async def send_prompt():
        llm_controller:LLMController = loader.resolve(config.controllers.get("llm_controller").get("name"))
        print(llm_controller)
        return await llm_controller.send_prompt()