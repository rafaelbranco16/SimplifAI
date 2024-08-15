controllers = {
    "document_controller": "DocumentController",
    "llm_controller":{
        "name":"LLMController",
        "path":"src.controllers.llm_controller"
    }
}

services = {
    "document_service":"DocumentService",
    "llm_service": {
        "name":"LLMService",
        "path":"src.services.llm_service"
    }
}

adapters = {
    "llm_adapter": {
        "name":"GPTAdapter",
        "path":"src.adapters.gpt_adapter"
    }
}

gpt_model = "gpt-4o"