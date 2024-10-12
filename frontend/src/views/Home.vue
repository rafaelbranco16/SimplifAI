<template>
    <div>
      <BlogCard />
      <AboutSection />
    </div>
  </template>
  
  <script>
  import BlogCard from '../components/blog_card/BlogCard.vue';
  import AboutSection from '../components/about_section/AboutSection.vue';
  
  export default {
    components: {
      BlogCard,
      AboutSection
    }
  }
  </script>
  
  <style scoped>
  </style>
  