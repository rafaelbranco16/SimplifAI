<template>
  <div id="entry-note" class="centered-container">
    <h1>Nota de entrada</h1>

    <section class="identification">
      <h2>Identificação</h2>
      <div class="form-group">
        <label for="nif">NIF:</label>
        <input type="text" id="nif" v-model="formData.nif"/>
      </div>
      <div class="form-group">
        <label for="name">Nome:</label>
        <input type="text" id="name" v-model="formData.name"/>
      </div>
      <div class="form-group">
        <label for="gender">Género:</label>
        <select id="gender" v-model="formData.gender">
          <option value="" disabled>Selecione o género...</option>
          <option>Masculino</option>
          <option>Feminino</option>
          <option>Outro</option>
        </select>
      </div>
      <div class="form-group">
        <label for="age">Idade:</label>
        <input type="number" id="age" v-model="formData.age"/>
      </div>
      <div class="form-group">
        <label for="cognitiveStatus">Estado cognitivo:</label>
        <input type="text" id="cognitiveStatus" v-model="formData.cognitiveStatus"/>
      </div>
      <div class="form-group">
        <label for="functionalStatus">Estado funcional:</label>
        <input type="text" id="functionalStatus" v-model="formData.functionalStatus"/>
      </div>
    </section>

    <section class="dynamic-fields">
      <h2>Alergias</h2>
      <div v-for="(allergy, index) in formData.allergies" :key="index" class="form-group">
        <input type="text" v-model="formData.allergies[index]" placeholder="Enter allergy" />
        <button @click="removeAllergy(index)">Remover</button>
      </div>
      <button @click="addAllergy">Adicionar</button>
    </section>

    <section class="background">
      <h2>Histórico médico</h2>
      <textarea v-model="formData.medicalBackground"></textarea>

      <h2>Histórico de cirurgias</h2>
      <textarea v-model="formData.surgicalBackground"></textarea>
    </section>

    <section class="dynamic-fields">
      <h2>Medicação</h2>
      <div v-for="(medication, index) in formData.medications" :key="index" class="form-group">
        <input type="text" v-model="medication.name" placeholder="Medicação"/>
        <input type="text" v-model="medication.dose" placeholder="Dose"/>
        <button @click="removeMedication(index)">Remover</button>
      </div>
      <button @click="addMedication">Adicionar</button>
    </section>

    <section class="sickness-history">
      <h2>História da doença atual</h2>
      <textarea v-model="formData.actualSicknessHistory"></textarea>
    </section>

    <section class="dynamic-fields">
      <h2>MCDTs</h2>
      <div v-for="(mcdt, index) in formData.mcdts" :key="index" class="form-group">
        <input type="text" v-model="mcdt.type"/>
        <input type="text" v-model="mcdt.text"/>
        <button @click="removeMCDT(index)">Remove</button>
      </div>
      <button @click="addMCDT">Adicionar</button>
    </section>

    <button class="submit-button" @click="submitForm">Enviar</button>
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
        medications: [],
        actualSicknessHistory: '',
        mcdts: [],
        nif: ''
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
    addMedication() {
      this.formData.medications.push({ name: '', dose: '' });
    },
    removeMedication(index) {
      this.formData.medications.splice(index, 1);
    },
    addMCDT() {
      this.formData.mcdts.push({ type: '', text: '' });
    },
    removeMCDT(index) {
      this.formData.mcdts.splice(index, 1);
    },
    async submitForm() {
      const submissionData = {
        allergies: this.formData.allergies.length > 0 ? this.formData.allergies : ["No allergies"],
        identification: {
          name: this.formData.name,
          gender: this.formData.gender,
          age: this.formData.age,
          cognitive_status: this.formData.cognitiveStatus,
          functional_status: this.formData.functionalStatus,
          nif: this.formData.nif
        },
        usual_medication: this.formData.medications.map(medication => ({
          medication: medication.name,
          dose: medication.dose
        })),
        personal_background: {
          medical_background: this.formData.medicalBackground,
          cirurgic_background: this.formData.surgicalBackground
        },
        actual_sickness_history: this.formData.actualSicknessHistory,
        mcdts: this.formData.mcdts.map(mcdt => ({
          type: mcdt.type,
          text: mcdt.text
        }))
      };

      try {
        const response = await fetch('http://localhost:8000/entry-note', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(submissionData)
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const result = await response.json();
        console.log('Form submitted successfully:', result);
        alert('A nota de entrada foi criada!');
      } catch (error) {
        console.error('There was a problem with the submission:', error);
        alert('Falha ao submeter.');
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
  