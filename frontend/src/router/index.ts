import { createRouter, createWebHistory } from 'vue-router'
import EntryNoteView from '@/views/EntryNoteView.vue'
import AudioView from '@/views/AudioView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'entry-note',
      component: EntryNoteView
    },
    {
      path: '/upload-audio',
      name: 'upload-audio',
      component: AudioView
    }
  ]
})

export default router
