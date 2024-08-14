from typing import List

class EntryNote:
    def __init__(self, allergies: List[str]):
        self.allergies = allergies  # List of allergies

    def __str__(self):
        return f"EntryNote(Allergies: {', '.join(self.allergies)})"

