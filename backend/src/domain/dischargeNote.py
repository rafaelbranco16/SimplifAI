class DischargeNote:
    def __init__(self, hospitalization_reason: str, therapeutic_proposal: str):
        self.hospitalization_reason = hospitalization_reason
        self.therapeutic_proposal = therapeutic_proposal

    def __str__(self):
        return f"DischargeNote(Hospitalization Reason: {self.hospitalization_reason}, Therapeutic Proposal: {self.therapeutic_proposal})"
