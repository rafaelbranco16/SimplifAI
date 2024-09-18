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
          <input v-model="dischargeData.allergies[0]" type="text" id="allergies" />
        </div>
  
        <!-- Identification Section -->
        <h3>Identification</h3>
        <div>
          <label for="name">Name:</label>
          <input v-model="dischargeData.identification.name" type="text" id="name" />
  
          <label for="gender">Gender:</label>
          <input v-model="dischargeData.identification.gender" type="text" id="gender" />
  
          <label for="age">Age:</label>
          <input v-model="dischargeData.identification.age" type="number" id="age" />
  
          <label for="cognitive_status">Cognitive Status:</label>
          <input v-model="dischargeData.identification.cognitive_status" type="text" id="cognitive_status" />
  
          <label for="functional_status">Functional Status:</label>
          <input v-model="dischargeData.identification.functional_status" type="text" id="functional_status" />
  
          <label for="nif_identification">NIF:</label>
          <input v-model="dischargeData.identification.nif" type="text" id="nif_identification" readonly />
        </div>
  
        <!-- Usual Medication Section -->
        <h3>Usual Medication</h3>
        <div v-for="(medication, index) in dischargeData.usual_medication" :key="index">
          <label for="medication">Medication:</label>
          <input v-model="medication.medication" type="text" id="medication" />
  
          <label for="dose">Dose:</label>
          <input v-model="medication.dose" type="text" id="dose" />
        </div>
  
        <!-- Personal Background Section -->
        <h3>Personal Background</h3>
        <div>
          <label for="medical_background">Medical Background:</label>
          <textarea v-model="dischargeData.personal_background.medical_background" id="medical_background"></textarea>
  
          <label for="cirurgic_background">Surgical Background:</label>
          <textarea v-model="dischargeData.personal_background.cirurgic_background" id="cirurgic_background"></textarea>
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
        }
      };
    },
    methods: {
      async submitForm() {
        try {
          // Make the GET request to your backend, passing the NIF in the request
          const response = await axios.get(`http://localhost:8000/entry-note/${this.nifInput}`);
          console.log(response.data)
          // Assuming the response data is in the same structure as dischargeData
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
  .discharge-note {
    max-width: 600px;
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
    background-color: #f9f9f9;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  label {
    display: block;
    margin: 0.5rem 0 0.2rem;
  }
  
  input, textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  h3 {
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
  }
  </style>
  