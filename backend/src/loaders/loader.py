from src.loaders.container import Container
from src.services.document_service import DocumentService
from src.controllers.document_controller import DocumentController
from src.adapters.gpt_adapter import GPTAdapter
from src import config
import importlib

loader = Container()

def load_class(module_path:str, class_name:str):
    module = importlib.import_module(module_path)
    return getattr(module, class_name)()

print("### Loading the Repos")
loader.register(
    "LLMAdapter", 
    load_class(
        config.adapters.get("llm_adapter").get("path"),
        config.adapters.get("llm_adapter").get("name")
    )
)

print("### Loading the Services")
loader.register("DocumentService", DocumentService())
loader.register(
    "LLMService", 
    load_class(
        config.services.get("llm_service").get("path"),
        config.services.get("llm_service").get("name")
    )
)

print("### Loading the Controllers")
loader.register("DocumentController", DocumentController())
loader.register(
    config.controllers["llm_controller"]["name"],
    load_class(
        config.controllers["llm_controller"]["path"],
        config.controllers["llm_controller"]["name"]
    ) 
)
