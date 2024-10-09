from src.domain.entry_note import EntryNote
from src.domain.identification import Identification
from src.domain.usual_medication import UsualMedication
from src.domain.personal_background import PersonalBackground

class EntryNoteMapper:
    @staticmethod
    def to_dict(entry_note: EntryNote) -> dict:
        """Converts an EntryNote object to a dictionary."""
        return entry_note.to_dict()

    @staticmethod
    def to_obj(entry_note_dict: dict) -> EntryNote:
        identification = Identification(
            name=entry_note_dict['identification']['name'],
            gender=entry_note_dict['identification']['gender'],
            age=entry_note_dict['identification']['age'],
            cognitive_status=entry_note_dict['identification']['cognitive_status'],
            functional_status=entry_note_dict['identification']['functional_status'],
            nif=entry_note_dict['identification']['nif']
        )

        usual_medication = [
            UsualMedication(
                medication=med['medication'],
                dose=med['dose']
            ) for med in entry_note_dict['usual_medication']
        ]

        personal_background = PersonalBackground(
            medical_background=entry_note_dict['personal_background']['medical_background'],
            cirurgic_background=entry_note_dict['personal_background']['cirurgic_background']
        )

        return EntryNote(
            id=entry_note_dict.get('id'),
            identification=identification,
            allergies=entry_note_dict['allergies'],
            usual_medication=usual_medication,
            personal_background=personal_background
        )

