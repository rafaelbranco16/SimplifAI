from logging import Logger


class DischargeText:
    def __init__(self,text:str):
        self.text = text
        Logger.print_info("New discharge note created")

    def __str__(self):
        return f"Discharge text:(Text: {self.text})"

    def to_dict(self):
        return {"discharge_text":self.text}