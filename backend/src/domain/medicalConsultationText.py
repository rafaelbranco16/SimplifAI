
class MedicalConsultationText:
    def __init__(self, text: str):
        self.text = text  # Text of the medical consultation

    def __str__(self):
        return f"MedicalConsultationText(Text: {self.text})"