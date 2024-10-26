<template>
  <div class="left-container">
    <!-- Controls for Recording and Uploading -->
     <h1>Nota de entrada</h1>
    <div class="controls">
      <button class="record-btn" @click="isRecording ? stopRecording() : startRecording()">
        {{ isRecording ? 'Parar gravação' : 'Começar gravação' }}
      </button>

      <audio v-if="audioURL" :src="audioURL" controls class="audio-player"></audio>

      <button class="upload-btn" @click="uploadAudio" :disabled="!audioURL">
        Enviar para tradução
      </button>

      <button class="send-btn" @click="sendTextToBackend" :disabled="!transcription">
        Preencher automaticamente
      </button>
    </div>

    <p v-if="transcription" class="transcription">
      Transcription: {{ transcription }}
    </p>

    <div v-if="jsonData" class="form">
      <h3>Editar Informações</h3>

      <label for="name">Nome:</label>
      <input v-model="jsonData.entry_note.identification.name" id="name" type="text" />

      <label for="gender">Gênero:</label>
      <input v-model="jsonData.entry_note.identification.gender" id="gender" type="text" />

      <label for="age">Idade:</label>
      <input v-model="jsonData.entry_note.identification.age" id="age" type="number" />

      <label for="cognitive_status">Estado Cognitivo:</label>
      <input v-model="jsonData.entry_note.identification.cognitive_status" id="cognitive_status" type="text" />

      <label for="functional_status">Estado Funcional:</label>
      <input v-model="jsonData.entry_note.identification.functional_status" id="functional_status" type="text" />

      <label for="nif">NIF:</label>
      <input v-model="jsonData.entry_note.identification.nif" id="nif" type="text" />

      <h4>Medicação Usual</h4>
      <div v-for="(medication, index) in jsonData.entry_note.usual_medication" :key="index" class="medication-item">
        <label :for="'medication' + index">Medicação {{ index + 1 }}:</label>
        <input v-model="jsonData.entry_note.usual_medication[index].medication" :id="'medication' + index" type="text" />

        <label :for="'dose' + index">Dose {{ index + 1 }}:</label>
        <input v-model="jsonData.entry_note.usual_medication[index].dose" :id="'dose' + index" type="text" />

        <button @click="removeMedication(index)" class="remove-btn">Remover Medicação</button>
      </div>

      <!-- Dynamic Allergies Fields -->
      <h4>Alergias</h4>
      <div v-for="(allergy, index) in jsonData.entry_note.allergies" :key="index" class="allergy-item">
        <label :for="'allergy' + index">Alergia {{ index + 1 }}:</label>
        <input v-model="jsonData.entry_note.allergies[index]" :id="'allergy' + index" type="text" />

        <button @click="removeAllergy(index)" class="remove-btn">Remover Alergia</button>
      </div>

      <!-- Personal Background Fields -->
      <label for="medical_background">Histórico Médico:</label>
      <input v-model="jsonData.entry_note.personal_background.medical_background" id="medical_background" type="text" />

      <label for="surgical_background">Histórico Cirúrgico:</label>
      <input v-model="jsonData.entry_note.personal_background.surgical_background" id="surgical_background" type="text" />

      <button class="send-btn" @click="sendUpdatedData">
        Enviar Dados Atualizados
      </button>
    </div>
  </div>
  <div class="right-container">
    <h1>Diário clínico</h1>
    <!-- Controls for Recording and Uploading -->
    <div class="controls">
      <button class="record-btn" @click="isRecording2 ? stopRecording2() : startRecording2()">
        {{ isRecording2 ? 'Parar gravação' : 'Começar gravação' }}
      </button>

      <audio v-if="audioURL2" :src="audioURL2" controls class="audio-player"></audio>

      <button class="upload-btn" @click="uploadAudio2" :disabled="!audioURL2">
        Enviar para tradução.
      </button>

      <button class="send-btn" @click="sendTextToBackend2" :disabled="!transcription2">
        Criar diário clínico
      </button>
    </div>

    <p v-if="transcription2" class="transcription">
      Transcription: {{ transcription2 }}
    </p>

  </div>
</template>

<script>
import config from '@/config';
import axios from 'axios';

export default {
  data() {
    return {
      isRecording: false,
      isRecording2: false,
      isRecording: false,
      isRecording2: false,
      audioChunks: [],
      audioChunks2: [],
      audioURL: null,
      audioURL2: null,
      transcription: null,
      transcription2: null,
      jsonData: null,
    };
  },
  methods: {
    async startRecording() {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);
      this.mediaRecorder.ondataavailable = (event) => {
        this.audioChunks.push(event.data);
      };
      this.mediaRecorder.onstop = () => {
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        this.audioURL = URL.createObjectURL(audioBlob);
      };
      this.audioChunks = [];
      this.mediaRecorder.start();
      this.isRecording = true;
    },
    stopRecording() {
      this.mediaRecorder.stop();
      this.isRecording = false;
    },
    async startRecording2() {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder2 = new MediaRecorder(stream);
      this.mediaRecorder2.ondataavailable = (event) => {
        this.audioChunks2.push(event.data);
      };
      this.mediaRecorder2.onstop = () => {
        const audioBlob = new Blob(this.audioChunks2, { type: 'audio/wav' });
        this.audioURL2 = URL.createObjectURL(audioBlob);
      };
      this.audioChunks2 = [];
      this.mediaRecorder2.start();
      this.isRecording2 = true;
    },
    stopRecording2() {
      this.mediaRecorder2.stop();
      this.isRecording2 = false;
    },
    async uploadAudio() {
      if (!this.audioChunks.length) return;

      const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
      const formData = new FormData();
      formData.append('file', audioBlob, 'audio.wav');

      try {
        const response = await axios.post(`${config.ip}/upload-audio`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
        this.transcription = response.data.transcription;

       
      } catch (error) {
        console.error('Error uploading audio:', error);
      }
    },
    async sendTextToBackend() {
      if (!this.transcription) return;
      try {
        const response = await axios.post(`${config.ip}/generate-entry-note/`, {
          "text":this.transcription
        });
        this.jsonData = response.data
        console.log('Texto enviado com sucesso!', response.data);
      } catch (error) {
        console.error('Erro ao enviar o texto:', error);
      }
    },
    async sendUpdatedData() {
      try {
        const response = await axios.post(`${config.ip}/entry-note`, this.jsonData.entry_note);
        console.log('Dados atualizados enviados com sucesso!', response.data);
      } catch (error) {
        console.error('Erro ao enviar dados atualizados:', error);
      }
    },
    async uploadAudio2() {
      if (!this.audioChunks2.length) return;

      const audioBlob = new Blob(this.audioChunks2, { type: 'audio/wav' });
      const formData = new FormData();
      formData.append('file', audioBlob, 'audio.wav');

      try {
        const response = await axios.post(`${config.ip}/upload-audio`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
        });
        this.transcription2 = response.data.transcription;

       
      } catch (error) {
        console.error('Error uploading audio:', error);
      }
    },
    async sendTextToBackend2() {
      if (!this.transcription2) return;
      try {
        const response = await axios.post(`${config.ip}/clinical-diary/`, {
          "id": this.jsonData.entry_note.identification.nif,
          "mct":this.transcription2
        });
        console.log('Texto enviado com sucesso!', response.data);
      } catch (error) {
        console.error('Erro ao enviar o texto:', error);
      }
    },
    
    removeMedication(index) {
      this.jsonData.entry_note.usual_medication.splice(index, 1);
    },
    removeAllergy(index) {
      this.jsonData.entry_note.allergies.splice(index, 1);
    }
  }
};
</script>

<style scoped>
/* Estilos do container geral */
.left-container {
  display: flex;
  float: left;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Arial', sans-serif;
  margin: 2%;
  margin-left: 10%;
  padding: 20px;
  max-width: 600px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.right-container {
  display: flex;
  float: right;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Arial', sans-serif;
  margin: 2%;
  margin-right: 10%;
  padding: 20px;
  max-width: 600px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
/* Estilos para os controles de gravação e upload */
.controls {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

/* Estilos para os botões */
.record-btn, .upload-btn, .send-btn {
  padding: 12px 20px;
  background-color: #4CAF50;
  width: 100%;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
  margin: 5px 0;
}

.record-btn:hover, .upload-btn:hover, .send-btn:hover {
  background-color: #45a049;
}

.upload-btn:disabled, .send-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
  margin-top: 20px;
}

.form label {
  font-weight: bold;
}

.form input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.transcription {
  margin-top: 20px;
  font-size: 14px;
  color: #333;
  background-color: #e8f5e9;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  text-align: center;
}
</style>
