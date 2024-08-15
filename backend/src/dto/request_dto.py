from pydantic import BaseModel

class RequestDto(BaseModel):
    prompt:str