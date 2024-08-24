import { createRouter, createWebHistory } from 'vue-router'
import EntryNoteView from '@/views/EntryNoteView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'entry-note',
      component: EntryNoteView
    },
  ]
})

export default router
