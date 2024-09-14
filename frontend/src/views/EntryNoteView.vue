<template>
    <div id="entry-note" class="centered-container">
      <h1>Entry Note</h1>
  
      <section class="identification">
        <h2>Identification</h2>
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="formData.name" placeholder="Enter name" />
        </div>
        <div class="form-group">
          <label for="gender">Gender:</label>
          <select id="gender" v-model="formData.gender">
            <option value="" disabled>Select gender</option>
            <option>Male</option>
            <option>Female</option>
            <option>Other</option>
          </select>
        </div>
        <div class="form-group">
          <label for="age">Age:</label>
          <input type="number" id="age" v-model="formData.age" placeholder="Enter age" />
        </div>
        <div class="form-group">
          <label for="cognitiveStatus">Cognitive Status:</label>
          <input type="text" id="cognitiveStatus" v-model="formData.cognitiveStatus" placeholder="Enter cognitive status" />
        </div>
        <div class="form-group">
          <label for="functionalStatus">Functional Status:</label>
          <input type="text" id="functionalStatus" v-model="formData.functionalStatus" placeholder="Enter functional status" />
        </div>
      </section>
  
      <section class="dynamic-fields">
        <h2>Allergies</h2>
        <div v-for="(allergy, index) in formData.allergies" :key="index" class="form-group">
          <!-- Use v-model for two-way binding to ensure the input stays in sync with the data -->
          <input type="text" v-model="formData.allergies[index]" placeholder="Enter allergy" />
          <button @click="removeAllergy(index)">Remove</button>
        </div>
        <button @click="addAllergy">Add Allergy</button>
      </section>
  
      <section class="background">
        <h2>Medical Background</h2>
        <textarea v-model="formData.medicalBackground" placeholder="Enter medical background"></textarea>
  
        <h2>Surgical Background</h2>
        <textarea v-model="formData.surgicalBackground" placeholder="Enter surgical background"></textarea>
      </section>
  
      <section class="dynamic-fields">
        <h2>Medications</h2>
        <div v-for="(medication, index) in formData.medications" :key="index" class="form-group">
          <!-- Use v-model for two-way binding to ensure data stays in sync with formData.medications -->
          <input type="text" v-model="medication.name" placeholder="Medication" />
          <input type="text" v-model="medication.dose" placeholder="Dose" />
          <button @click="removeMedication(index)">Remove</button>
        </div>
        <button @click="addMedication">Add Medication</button>
      </section>
  
      <button class="submit-button" @click="submitForm">Submit</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          name: '',
          gender: '',
          age: null,
          cognitiveStatus: '',
          functionalStatus: '',
          allergies: [],
          medicalBackground: '',
          surgicalBackground: '',
          medications: []
        }
      };
    },
    methods: {
      addAllergy() {
        this.formData.allergies.push('');
      },
      removeAllergy(index) {
        this.formData.allergies.splice(index, 1);
      },
      updateAllergy(index, value) {
        this.$set(this.formData.allergies, index, value);
      },
      addMedication() {
        this.formData.medications.push({ name: '', dose: '' });
      },
      removeMedication(index) {
        this.formData.medications.splice(index, 1);
      },
      updateMedication(index, field, value) {
        this.$set(this.formData.medications[index], field, value);
      },
      async submitForm() {
        // Create the JSON object with the desired structure
        const submissionData = {
          allergies: this.formData.allergies.length > 0 ? this.formData.allergies : ["No allergies"],
          identification: {
            name: this.formData.name,
            gender: this.formData.gender,
            age: this.formData.age,
            cognitive_status: this.formData.cognitiveStatus,
            functional_status: this.formData.functionalStatus
          },
          usual_medication: this.formData.medications.map(medication => ({
            medication: medication.name,
            dose: medication.dose
          })),
          personal_background: {
            medical_background: this.formData.medicalBackground,
            cirurgic_background: this.formData.surgicalBackground
          }
        };

        try {
          // Perform the POST request using fetch
          const response = await fetch('http://localhost:8000/entry-note', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(submissionData)  // Send the JSON data
          });

          // Check if the response was successful
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }

          // Parse the JSON response (if any)
          const result = await response.json();
          console.log('Form submitted successfully:', result);
          alert('Form submitted successfully!');

        } catch (error) {
          // Handle errors (network errors, invalid response, etc.)
          console.error('There was a problem with the submission:', error);
          alert('Failed to submit the form.');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .centered-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    background-color: var(--color-background);
    color: var(--color-text);
    min-height: 100vh;
    width: 100%;
    box-sizing: border-box;
  }
  
  h1 {
    margin-bottom: 2rem;
    font-size: 2.5rem;
  }
  
  h2 {
    margin-top: 2rem;
    margin-bottom: 1rem;
    font-size: 1.5rem;
    color: var(--color-heading);
  }
  
  .form-group {
    margin-bottom: 1.5rem;
    width: 100%;
    max-width: 600px; /* Center within the available space */
    display: flex;
    align-items: center;
  }
  
  label {
    flex: 1;
    margin-right: 1rem;
    text-align: right;
  }
  
  input[type="text"],
  input[type="number"],
  select,
  textarea {
    flex: 2;
    padding: 0.5rem;
    border: 1px solid var(--color-border);
    border-radius: 4px;
    font-size: 1rem;
    width: 100%;
    box-sizing: border-box;
  }
  
  textarea {
    resize: vertical;
    min-height: 100px;
  }
  
  button {
    margin-left: 1rem;
    padding: 0.5rem 1rem;
    background-color: hsla(160, 100%, 37%, 1);
    color: var(--vt-c-white);
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: hsla(160, 100%, 37%, 0.8);
  }
  
  .submit-button {
    margin-top: 2rem;
    padding: 1rem 2rem;
    background-color: var(--vt-c-indigo);
    color: white;
    font-size: 1.25rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
    max-width: 600px; /* Center submit button within the form */
  }
  
  .submit-button:hover {
    background-color: var(--vt-c-black-soft);
  }
  </style>
  