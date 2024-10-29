<template>
  <div class="discharge-note">
    <h1>Nota de alta</h1>

    <!-- Form to Enter NIF -->
    <div class="nif-form">
      <label for="nif">Enter NIF:</label>
      <input v-model="nifInput" type="text" id="nif" placeholder="Enter NIF" />
      <button class="submit-button" @click="submitForm">Enviar</button>
    </div>

    <!-- Display Discharge Note Form if NIF is valid -->
    <div v-if="formVisible" class="discharge-form">
      <h2>Informação de alta</h2>

      <!-- Allergies -->
      <div>
        <label for="allergies">Alergias:</label>
        <input v-model="dischargeData.entry_note.allergies[0]" type="text" id="allergies" />
      </div>

      <!-- Identification Section -->
      <h3>Identificação</h3>
      <div>
        <label for="name">Nome:</label>
        <input v-model="dischargeData.entry_note.identification.name" type="text" id="name" />

        <label for="gender">Género:</label>
        <input v-model="dischargeData.entry_note.identification.gender" type="text" id="gender" />

        <label for="age">Idade:</label>
        <input v-model="dischargeData.entry_note.identification.age" type="number" id="age" />

        <label for="cognitive_status">Estado cognitivo:</label>
        <input v-model="dischargeData.entry_note.identification.cognitive_status" type="text" id="cognitive_status" />

        <label for="functional_status">Estado funcional:</label>
        <input v-model="dischargeData.entry_note.identification.functional_status" type="text" id="functional_status" />

        <label for="nif_identification">NIF:</label>
        <input v-model="dischargeData.entry_note.identification.nif" type="text" id="nif_identification" readonly />
      </div>

      <!-- Usual Medication Section -->
      <h3>Medicação usual</h3>
      <div v-for="(medication, index) in dischargeData.entry_note.usual_medication" :key="index">
        <label for="medication">Medicação:</label>
        <input v-model="medication.medication" type="text" id="medication" />

        <label for="dose">Dose:</label>
        <input v-model="medication.dose" type="text" id="dose" />
      </div>

      <!-- Personal Background Section -->
      <h3>Antecedentes pessoais</h3>
      <div>
        <label for="medical_background">Histórico médico:</label>
        <textarea v-model="dischargeData.entry_note.personal_background.medical_background" id="medical_background"></textarea>

        <label for="cirurgic_background">Histórico cirúrgico:</label>
        <textarea v-model="dischargeData.entry_note.personal_background.cirurgic_background" id="cirurgic_background"></textarea>
      </div>

      <!-- Discharge Text -->
      <h3>Nota de alta</h3>
      <div>
        <textarea v-model="dischargeData.discharge_text" id="discharge_text" readonly></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      nifInput: '',
      formVisible: false,
      dischargeData: {
        entry_note: {
          allergies: ["No allergies"],
          identification: {
            name: "",
            gender: "",
            age: null,
            cognitive_status: "",
            functional_status: "",
            nif: ""
          },
          usual_medication: [
            {
              medication: "",
              dose: ""
            }
          ],
          personal_background: {
            medical_background: "",
            cirurgic_background: ""
          },
          actual_sickness_history: "",
          mcdts: [
            {
              type:"",
              text: ""  
            }
          ]
        },
        discharge_text: "" // Holds the discharge summary
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        // Make the POST request to your backend, passing the NIF in the request body
        const response = await axios.post(`http://localhost:8000/discharge-note`, {
          nif: this.nifInput
        });
        console.log(response.data);
        // Assuming the response data contains the dischargeData structure
        if (response.data) {
          this.dischargeData = response.data.message;
          this.formVisible = true; // Show the form after receiving the data
        } else {
          this.formVisible = false;
          alert("Sem dados para o NIF.");
        }
      } catch (error) {
        console.error("Error fetching discharge note:", error);
        alert("Erro ao obter os dados.");
      }
    }
  }
};
</script>
<style scoped>

body {
  background-color: black;
  color: white;
}

.discharge-note {
  max-width: 800px;
  margin: 2% auto;
}

.nif-form {
  margin-bottom: 1.5rem;
}

.submit-button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.discharge-form {
  background-color: #222;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1);
}

label {
  display: block;
  margin: 0.5rem 0 0.2rem;
  color: #fff;
}

input, textarea {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1.5rem;
  border: 1px solid #555;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
}
h2, h3 {
  color: #fff;
}

#discharge_text {
  height: 300px;
  background-color: #333;
  color: #fff;
}

h3 {
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}
</style>
