<template>
    <div>
      <button @click="isRecording ? stopRecording() : startRecording()">
        {{ isRecording ? 'Stop Recording' : 'Start Recording' }}
      </button>
      
      <audio v-if="audioURL" :src="audioURL" controls></audio>
      
      <button @click="uploadAudio" :disabled="!audioURL">Upload Audio for Transcription</button>
  
      <p v-if="transcription">Transcription: {{ transcription }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        isRecording: false,
        mediaRecorder: null,
        audioChunks: [],
        audioURL: null,
        transcription: null,
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
      async uploadAudio() {
        if (!this.audioChunks.length) return;
  
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        const formData = new FormData();
        formData.append('file', audioBlob, 'audio.wav');
  
        try {
          const response = await axios.post('http://localhost:8000/upload-audio', formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
          });
          this.transcription = response.data.transcription;
        } catch (error) {
          console.error('Error uploading audio:', error);
        }
      },
    },
  };
  </script>
  