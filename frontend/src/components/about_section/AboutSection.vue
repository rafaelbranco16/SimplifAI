<template>
  <div class="about-section-container">
    <h2 @click="toggleExpand">About Us!</h2>
    <p v-if="expanded">
      No âmbito do Prémio Digital 24 Siemens – SimplifAI, a nossa equipa abraçou o desafio de melhorar a eficiência dos profissionais de saúde, reduzindo a burocracia que frequentemente desvia tempo da prática clínica e prejudica a qualidade da relação médico-paciente. Este projeto visa desenvolver uma prova de conceito que simplifica processos administrativos como a criação de notas de alta a partir de notas de entrada e diários clínicos e automatização do registo de um diário de consulta, através de técnicas avançadas de Processamento de Linguagem Natural (NLP). Estamos a explorar abordagens com algoritmos avançados para a execução de tarefas como sumarização, conversão de fala em texto (speech-to-text) com atenção à narrativa, e análise de tópicos e AI generativa, com o apoio de Large Language Models (LLMs).
      A nossa equipa é composta por 2 estudantes da Escola Superior de Engenharia do Porto (ISEP), 1 Professor orientador da mesma instituição, e um expert-in-the-loop médico que traz uma perspectiva clínica essencial tanto para o projeto como para a avaliação da solução. Cada membro aporta uma visão única para transformar este desafio em realidade:
      <br/><br/>
      Rafael Branco – Engenheiro informático formado no ISEP e atualmente a trabalhar como analista SOC Júnior. Conta também com o curso básico de música feito no Conservatório de Música do Porto.
      <br/>
      Filipe Ferreira – Engenheiro informático formado no ISEP e atualmente a trabalhar como <i>Software Developer</i>
      <br/>
      Orientador - Tiago Dias  – Professor Assistente Convidado no ISEP a lecionar Arquitetura de Software e Organanização de Desenvolvimento de Software e Machine Learning Engineer na Liminal com mestrado na área da Engenharia de Inteligência Artificial. Nos tempos livres anda de bicicleta, toca guitarra numa banda e compõe.
      <br/>
      Médico - André Dias – Médico Interno de Formação Geral na ULS Matosinhos, com experiência em criação de registos clínicos e observação de doentes. Experiência como investigador no GECAD, colaborando com input médico aliado ao uso de inteligência artificial. Guitarrista e Ciclista em desenvolvimento.
      <br/><br/>
      Estamos comprometidos com o uso de tecnologia para apoiar a prática médica, poupando tempo e permitindo que os profissionais de saúde foquem mais no que realmente importa: o bem-estar dos seus pacientes.
    </p>
    
    <div v-if="expanded" class="download-buttons-container">
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

    <button @click="toggleExpand" class="toggle-button">
      {{ expanded ? 'Mostrar Menos' : 'Mostrar Mais' }}
    </button>
  </div>
</template>

<script>
import DownloadButton from '../download_button/DownloadButton.vue'; // Ajuste o caminho conforme necessário

export default {
  name: 'AboutSection',
  components: {
    DownloadButton
  },
  data() {
    return {
      expanded: false,
    };
  },
  methods: {
    toggleExpand() {
      this.expanded = !this.expanded;
    },
  }
}
</script>

<style scoped>
.about-section-container {
  background-color: #333;
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

.toggle-button {
  margin-top: 15px;
  padding: 8px 16px;
  background-color: #444;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

.toggle-button:hover {
  background-color: #666;
}
</style>
