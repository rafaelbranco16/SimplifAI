<template>
  <div class="discharge-note">
    <h1>Discharge Note</h1>

    <!-- Form to Enter NIF -->
    <div class="nif-form">
      <label for="nif">Enter NIF:</label>
      <input v-model="nifInput" type="text" id="nif" placeholder="Enter NIF" />
      <button class="submit-button" @click="submitForm">Submit</button>
    </div>

    <!-- Display Discharge Note Form if NIF is valid -->
    <div v-if="formVisible" class="discharge-form">
      <h2>Discharge Information</h2>

      <!-- Allergies -->
      <div>
        <label for="allergies">Allergies:</label>
        <input v-model="dischargeData.entry_note.allergies[0]" type="text" id="allergies" />
      </div>

      <!-- Identification Section -->
      <h3>Identification</h3>
      <div>
        <label for="name">Name:</label>
        <input v-model="dischargeData.entry_note.identification.name" type="text" id="name" />

        <label for="gender">Gender:</label>
        <input v-model="dischargeData.entry_note.identification.gender" type="text" id="gender" />

        <label for="age">Age:</label>
        <input v-model="dischargeData.entry_note.identification.age" type="number" id="age" />

        <label for="cognitive_status">Cognitive Status:</label>
        <input v-model="dischargeData.entry_note.identification.cognitive_status" type="text" id="cognitive_status" />

        <label for="functional_status">Functional Status:</label>
        <input v-model="dischargeData.entry_note.identification.functional_status" type="text" id="functional_status" />

        <label for="nif_identification">NIF:</label>
        <input v-model="dischargeData.entry_note.identification.nif" type="text" id="nif_identification" readonly />
      </div>

      <!-- Usual Medication Section -->
      <h3>Usual Medication</h3>
      <div v-for="(medication, index) in dischargeData.entry_note.usual_medication" :key="index">
        <label for="medication">Medication:</label>
        <input v-model="medication.medication" type="text" id="medication" />

        <label for="dose">Dose:</label>
        <input v-model="medication.dose" type="text" id="dose" />
      </div>

      <!-- Personal Background Section -->
      <h3>Personal Background</h3>
      <div>
        <label for="medical_background">Medical Background:</label>
        <textarea v-model="dischargeData.entry_note.personal_background.medical_background" id="medical_background"></textarea>

        <label for="cirurgic_background">Surgical Background:</label>
        <textarea v-model="dischargeData.entry_note.personal_background.cirurgic_background" id="cirurgic_background"></textarea>
      </div>

      <!-- Discharge Text -->
      <h3>Discharge Text</h3>
      <div>
        <label for="discharge_text">Discharge Summary:</label>
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
      nifInput: '', // Stores the entered NIF value
      formVisible: false, // Controls visibility of the discharge form
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
          }
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
          alert("No data found for the given NIF.");
        }
      } catch (error) {
        console.error("Error fetching discharge note:", error);
        alert("Failed to retrieve data from the backend.");
      }
    }
  }
};
</script>
<style scoped>
/* Set background color to black and text color to white */
body {
  background-color: black;
  color: white;
}

.discharge-note {
  max-width: 800px; /* Increase the width of the discharge note section */
  margin: 0 auto;
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
  background-color: #222; /* Darker background for the form */
  padding: 2rem; /* Increase padding for more space */
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(255, 255, 255, 0.1); /* Subtle white shadow */
}

label {
  display: block;
  margin: 0.5rem 0 0.2rem;
  color: #fff; /* Make label text white */
}

input, textarea {
  width: 100%;
  padding: 0.75rem; /* Increase padding for inputs */
  margin-bottom: 1.5rem; /* More spacing between elements */
  border: 1px solid #555; /* Darker border for inputs */
  border-radius: 4px;
  background-color: #333; /* Darker background for inputs */
  color: #fff; /* Make input text white */
}

h1, h2, h3 {
  color: #fff; /* Set headings to white */
}

#discharge_text {
  height: 300px; /* Increase height of discharge summary box */
  background-color: #333; /* Darker background for textarea */
  color: #fff; /* White text inside textarea */
}

h3 {
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}
</style>
