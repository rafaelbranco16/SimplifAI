<template>
  <div class="download-button" @click="toggleDropdown">
    <p class="description">{{ description }}</p>
    <img class="download-icon" src="@/assets/download-icon.png" alt="Download" />
    <div v-if="isDropdownOpen" class="dropdown">
      <ul>
        <li v-for="file in files" :key="file.name">
          <a :href="file.link" target="_blank">{{ file.name }}</a>
        </li>
      </ul>
    </div>
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
    files: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      isDropdownOpen: false
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
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
  position: relative; /* Para que o dropdown fique posicionado corretamente */
}

.download-button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.download-icon {
  width: 20px;
  height: 20px;
}

.dropdown {
  position: absolute; /* Faz o dropdown aparecer em relação ao botão */
  background-color: white;
  color: black;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 5px;
  z-index: 1000; /* Para garantir que fique acima de outros elementos */
  width: 100%; /* Para que o dropdown tenha a mesma largura do botão */
}

.dropdown ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dropdown li {
  padding: 10px;
}

.dropdown li a {
  text-decoration: none;
  color: black;
}

.dropdown li:hover {
  background-color: #f0f0f0; /* Cor ao passar o mouse */
}
</style>
