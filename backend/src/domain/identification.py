from typing import List
class Identification:
    def __init__(self, gender: str, age: int, cognitive_status: str, function_status: str):
        self.gender = gender  # Gender of the patient
        self.age = age  # Age of the patient
        self.cognitive_status = cognitive_status  # Cognitive status of the patient
        self.function_status = function_status  # Functional status of the patient

    def __str__(self):
        return (f"Identification(Gender: {self.gender}, Age: {self.age}, "
                f"Cognitive Status: {self.cognitive_status}, Function Status: {self.function_status})")

