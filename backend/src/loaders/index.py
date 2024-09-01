from src import config

controllers = [
    config.document_controller,
    config.medical_controller,
    config.llm_controller
]

services = [
    config.llm_service,
    config.document_service,
    config.medical_service
]

adapters = [
    config.llm_adapter
]