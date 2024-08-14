from typing import List
class UsualMedication:
    def __init__(self, medication: List[str], dose: List[str]):
        self.medication = medication
        self.dose = dose

    def __str__(self):
        meds = [f"{med} ({d})" for med, d in zip(self.medication, self.dose)]
        return f"UsualMedication(Medications: {', '.join(meds)})"
    