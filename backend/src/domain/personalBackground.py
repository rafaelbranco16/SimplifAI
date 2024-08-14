from typing import List
class PersonalBackground:
    def __init__(self, medical_background: List[str], cirurgic_background: List[str]):
        self.medical_background = medical_background  # List of medical background details
        self.cirurgic_background = cirurgic_background  # List of surgical background details

    def __str__(self):
        medical_background_str = "; ".join(self.medical_background)
        cirurgic_background_str = "; ".join(self.cirurgic_background)
        return (f"PersonalBackground(Medical Background: {medical_background_str}, "
                f"Surgical Background: {cirurgic_background_str})")

