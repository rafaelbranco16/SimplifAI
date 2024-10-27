import { createRouter, createWebHistory } from 'vue-router'
import EntryNoteView from '@/views/EntryNoteView.vue'
import AudioView from '@/views/AudioView.vue'
import DischargeNoteView from '@/views/DischargeNoteView.vue'
import Home from '@/views/Home.vue'
import ClinicalHistory from '@/views/ClinicalHistory.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path:'/home',
      name:'home',
      component:Home
    },
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
    },
    {
      path: '/clinical-history',
      name: 'clinical-history',
      component: ClinicalHistory
    }
  ]
})

export default router
