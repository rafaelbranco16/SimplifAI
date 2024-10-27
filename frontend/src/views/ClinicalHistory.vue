<template>
  <div class="clinical-history-container">
    <h1>História Clínica</h1>
    <div class="controls">
      <button class="record-btn" @click="isRecording2 ? stopRecording2() : startRecording2()">
        {{ isRecording2 ? 'Parar gravação' : 'Começar gravação' }}
      </button>

      <audio v-if="audioURL2" :src="audioURL2" controls class="audio-player"></audio>

      <button class="upload-btn" @click="uploadAudio2" :disabled="!audioURL2">
        Enviar para tradução
      </button>
      <input v-model="nif" type="text" id="nif" />

      <button class="send-btn" @click="sendTextToBackend2" :disabled="!transcription2">
        Criar diário clínico
      </button>
    </div>

    <textarea v-model="transcription2" class="transcription" placeholder="Escreva aqui ou grave para preencher..."></textarea>
  </div>
</template>

<script>
import config from '@/config';
import axios from 'axios';

export default {
  data() {
    return {
      isRecording2: false,
      audioChunks2: [],
      audioURL2: null,
      transcription2: null,
      nif: ""
    };
  },
  methods: {
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
        const response = await axios.post(`${config.ip}/clinical-history/`, {
          "id": this.nif,
          "mct": this.transcription2
        });
        console.log('Texto enviado com sucesso!', response.data);
      } catch (error) {
        console.error('Erro ao enviar o texto:', error);
      }
    }
  }
};
</script>

<style scoped>
.clinical-history-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Arial', sans-serif;
  margin: 2% auto;
  padding: 20px;
  max-width: 600px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.controls {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

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
