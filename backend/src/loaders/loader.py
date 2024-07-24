from src.loaders.container import Container
from src.services.document_service import DocumentService
from src.controllers.document_controller import DocumentController

loader = Container()

print("### Loading the Services")
loader.register("DocumentService", DocumentService())

print("### Loading the Controllers")
loader.register("DocumentController", DocumentController())

print("### Loading the Repos")