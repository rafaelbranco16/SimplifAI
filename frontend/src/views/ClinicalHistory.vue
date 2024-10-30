<template>
  <div class="clinical-history-container">
    <h1>Consultas</h1>
    <div class="controls">
      <button class="record-btn" @click="isRecording2 ? stopRecording2() : startRecording2()">
        {{ isRecording2 ? 'Parar gravação' : 'Começar gravação' }}
      </button>

      <audio v-if="audioURL2" :src="audioURL2" controls class="audio-player"></audio>

      <button class="upload-btn" @click="uploadAudio2" :disabled="!audioURL2">
        Enviar para tradução
      </button>
      <input v-model="nif" type="text" id="nif" class="input-field" placeholder="Enter NIF" />

      <button class="send-btn" @click="sendTextToBackend2" :disabled="!transcription2">
        Criar diário de consulta
      </button>
    </div>

    <textarea v-model="transcription2" class="transcription" placeholder="Escreva aqui ou grave para preencher..."></textarea>
    <textarea v-model="final_text" class="transcription" placeholder="Diário da consulta..."></textarea>

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
      nif: "",
      final_text:""
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
        window.alert('Erroa ao enviar o audio.');
      }
    },
    async sendTextToBackend2() {
      if (!this.transcription2) return;
      try {
        const response = await axios.post(`${config.ip}/clinical-history/`, {
          "id": this.nif,
          "mct": this.transcription2
        });
        this.final_text = response.data.message.medical_consultation_text.text;
      } catch (error) {
        window.alert('Erro ao enviar o texto:', error);
      }
    }
  }
};
</script>

<style scoped>
.clinical-history-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background-color: var(--color-background, #333);
  color: var(--color-text, #f5f5f5);
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: var(--color-heading, #f5f5f5);
}

.controls {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  width: 100%;
}

.record-btn, .upload-btn, .send-btn {
  padding: 0.75rem 1.25rem;
  font-size: 1rem;
  color: #fff;
  background-color: hsla(160, 100%, 37%, 1);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 0.5rem 0;
  transition: background-color 0.3s ease;
}

.record-btn:hover, .upload-btn:hover, .send-btn:hover {
  background-color: hsla(160, 100%, 37%, 0.8);
}

.record-btn:disabled, .upload-btn:disabled, .send-btn:disabled {
  background-color: #555;
  cursor: not-allowed;
}

.input-field, .transcription {
  width: 100%;
  padding: 0.75rem;
  margin: 0.5rem 0;
  border: 1px solid var(--color-border, #777);
  border-radius: 4px;
  background-color: #444;
  color: #fff;
  font-size: 1rem;
  box-sizing: border-box;
}

.transcription {
  resize: vertical;
  min-height: 100px;
}
</style>
