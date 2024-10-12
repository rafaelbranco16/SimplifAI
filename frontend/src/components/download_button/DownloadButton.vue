<template>
    <div class="download-button" @click="handleClick">
      <p class="description">{{ description }}</p>
      <img class="download-icon" src="@/assets/download-icon.png" alt="Download" />
    </div>
  </template>
  
  <script>
  export default {
    name: 'DownloadButton',
    props: {
      description: {
        type: String,
        required: true
      },
      link: {
        type: String,
        required: true
      }
    },
    methods: {
      handleClick() {
        window.open(this.link, '_blank');
      }
    }
  }
  </script>
  
  <style scoped>
  .download-button {
    background-color: #28a745;
    color: white;
    border-radius: 8px;
    padding: 5px;
    margin: 10px;
    width: 200px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  
  .download-button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }
  
  .download-icon {
    width: 20px;
    height: 20px;
  }
  </style>
  