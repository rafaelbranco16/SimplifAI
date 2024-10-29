<template>
  <div class="about-section-container">
    <h2>Bem-vindo à nossa seção!</h2>
    <p>About Us!</p>
    
    <div class="download-buttons-container">
      <DownloadButton 
        description="Notas de Entrada" 
        :files="[
          { name: 'Nota de Entrada 1', link: '/pdfs/entry_notes/entry_note_1.pdf' },
          { name: 'Nota de Entrada 3', link: '/pdfs/entry_notes/entry_note_2.pdf' },
          { name: 'Nota de Entrada 4', link: '/pdfs/entry_notes/entry_note_3.pdf' },
          { name: 'Nota de Entrada 5', link: '/pdfs/entry_notes/entry_note_4.pdf' }
        ]"
      />
      <DownloadButton 
        description="Diários Clínicos" 
        :files="[
          { name: 'Diário Clínico 1', link: '/pdfs/clinical_diaries/clinical_diary_1.pdf' },
          { name: 'Diário Clínico 3', link: '/pdfs/clinical_diaries/clinical_diary_2.pdf' },
          { name: 'Diário Clínico 4', link: '/pdfs/clinical_diaries/clinical_diary_3.pdf' },
          { name: 'Diário Clínico 5', link: '/pdfs/clinical_diaries/clinical_diary_4.pdf' }
        ]"
      />
      <DownloadButton 
        description="Notas de Alta" 
        :files="[
          { name: 'Nota de Alta 1', link: '/pdfs/discharge_notes/discharge_note_1.pdf' },
          { name: 'Nota de Alta 4', link: '/pdfs/discharge_notes/discharge_note_3.pdf' }
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
