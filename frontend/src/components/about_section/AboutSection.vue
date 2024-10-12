<template>
    <div class="about-section-container">
      <h2>Bem-vindo à nossa seção!</h2>
      <p>ABout US!</p>
      
      <div class="download-buttons-container">
        <DownloadButton 
          description="Notas de Entrada" 
          link="/path/to/report.pdf" 
        />
        <DownloadButton 
          description="Diários Clínicos" 
          link="/path/to/data.csv" 
        />
        <DownloadButton 
          description="Notas de Alta" 
          link="/path/to/document.docx" 
        />
      </div>
    </div>
  </template>
  
  <script>
  import DownloadButton from '../download_button/DownloadButton.vue';
  
  export default {
    name: 'AboutSection',
    components: {
      DownloadButton
    }
  }
  </script>
  
  <style scoped>
  .about-section-container {
    background-color: black;
    color: white;
    height: auto;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  
  .download-buttons-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  </style>
  