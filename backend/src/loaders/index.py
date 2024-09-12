from src import config

controllers = [
    config.document_controller,
    config.medical_controller,
    config.llm_controller,
    config.entry_note_controller
]

services = [
    config.llm_service,
    config.document_service,
    config.medical_service,
    config.entry_note_service
]

adapters = [
    config.llm_adapter,
    config.entry_note_adapter,
    config.clinical_diary_adapter
]