from src.loaders import loader
from src import config
class MedicalController:
    def __init__(self) -> None:
        self.service = loader.loader.resolve(config.medical_service["name"])

    async def generate_medical_consultation():
        raise NotImplementedError("Not Implemented Yet...")