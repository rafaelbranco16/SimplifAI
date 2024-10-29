<template>
  <div id="app">
    <nav class="navbar">
      <div class="logo">
        <router-link to="/">SimplifAI</router-link>
      </div>

      <div class="menu" @click="toggleMenu">
        <span class="menu-icon" :class="{'is-active': isActive}"></span>
      </div>

      <ul class="nav-links" :class="{'show': isActive}">
        <li><router-link to="/" @click="closeMenu">Home</router-link></li>
        <li><router-link to="/entry-note" @click="closeMenu">Nota de Entrada</router-link></li>
        <li><router-link to="/upload-audio" @click="closeMenu">Diário Clínico</router-link></li>
        <li><router-link to="/discharge-note" @click="closeMenu">Nota de Alta</router-link></li>
        <li><router-link to="/clinical-history" @click="closeMenu">Consultas</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isActive = !this.isActive;
    },
    closeMenu() {
      this.isActive = false;
    }
  }
}
</script>

<style scoped>
/* Basic reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
}

/* Navigation Styles */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 1rem 2rem;
}

.logo a {
  color: white;
  font-size: 1.5rem;
  text-decoration: none;
  font-weight: bold;
}

.menu {
  display: none;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li {
  margin-left: 2rem;
}

.nav-links li a {
  color: white;
  text-decoration: none;
  font-size: 1rem;
}

.nav-links li a:hover {
  text-decoration: underline;
}

/* Responsive styles */
@media (max-width: 768px) {
  .menu {
    display: block;
    cursor: pointer;
  }

  .menu-icon {
    width: 25px;
    height: 3px;
    background-color: white;
    position: relative;
    transition: all 0.3s ease;
  }

  .menu-icon::before,
  .menu-icon::after {
    content: '';
    width: 25px;
    height: 3px;
    background-color: white;
    position: absolute;
    left: 0;
    transition: all 0.3s ease;
  }

  .menu-icon::before {
    top: -8px;
  }

  .menu-icon::after {
    top: 8px;
  }

  .is-active {
    background-color: transparent;
  }

  .is-active::before {
    transform: rotate(45deg);
    top: 0;
  }

  .is-active::after {
    transform: rotate(-45deg);
    top: 0;
  }

  .nav-links {
    position: absolute;
    top: 60px;
    right: 0;
    background-color: #333;
    width: 100%;
    height: 100vh;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    display: none;
  }

  .nav-links li {
    margin: 2rem 0;
  }

  .nav-links.show {
    display: flex;
  }
}
</style>
