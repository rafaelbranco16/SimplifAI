from typing import List

class HospitalizationProblems:
    def __init__(self, admission_history: List[str], mcdt: str, evolution: str, final_state: str):
        self.admission_history = admission_history  # List of admission history entries
        self.mcdt = mcdt  # Medical, Clinical, Diagnostic Tests
        self.evolution = evolution  # Progress or course of the illness
        self.final_state = final_state  # Final condition or state of the patient

    def __str__(self):
        # Format the list of admission history as a string with each entry on a new line
        admission_history_str = "\n".join(self.admission_history)
        return (f"HospitalizationProblems(Admission History: \n{admission_history_str}\n"
                f"MCDT: {self.mcdt}, Evolution: {self.evolution}, Final State: {self.final_state})")
