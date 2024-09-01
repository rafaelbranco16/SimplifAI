from typing import List

class EntryNote:
    def __init__(self, identification, allergies: List[str]):
        self.allergies = allergies
        self.identification = identification

    def __str__(self):
        return f"EntryNote(Allergies: {', '.join(self.allergies)})"

