<template>
  <div class="about-section-container">
    <h2>Bem-vindo à nossa seção!</h2>
    <p>About Us!</p>
    
    <div class="download-buttons-container">
      <DownloadButton 
        description="Notas de Entrada" 
        :files="[
          { name: 'Nota de Entrada 1', link: '/pdfs/discharge_note_1.pdf' },
          { name: 'Nota de Entrada 2', link: '/pdfs/discharge_note_2.pdf' }
        ]"
      />
      <DownloadButton 
        description="Diários Clínicos" 
        :files="[
          { name: 'Diário Clínico 1', link: '/path/to/data1.csv' },
          { name: 'Diário Clínico 2', link: '/path/to/data2.csv' }
        ]"
      />
      <DownloadButton 
        description="Notas de Alta" 
        :files="[
          { name: 'Nota de Alta 1', link: '/path/to/document1.docx' },
          { name: 'Nota de Alta 2', link: '/path/to/document2.docx' }
        ]"
      />
    </div>
  </div>
</template>

<script>
import DownloadButton from '../download_button/DownloadButton.vue'; // Ajuste o caminho conforme necessário

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
