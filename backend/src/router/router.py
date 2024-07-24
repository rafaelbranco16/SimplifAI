from fastapi import APIRouter
from src.loaders.loader import loader
from src.controllers.document_controller import DocumentController
from src import config

router = APIRouter()

class Router:
    @router.get("/")
    async def default():
        document_loader_controller:DocumentController = loader.resolve(config.controllers["document_controller"]) 
        return await document_loader_controller.default()