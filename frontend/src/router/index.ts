import { createRouter, createWebHistory } from 'vue-router'
import EntryNoteView from '@/views/EntryNoteView.vue'
import AudioView from '@/views/AudioView.vue'
import DischargeNoteView from '@/views/DischargeNoteView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/entry-note',
      name: 'entry-note',
      component: EntryNoteView
    },
    {
      path: '/upload-audio',
      name: 'upload-audio',
      component: AudioView
    },
    {
      path: '/discharge-note',
      name: 'discharge-note',
      component: DischargeNoteView
    }
  ]
})

export default router
