import { createRouter, createWebHistory } from 'vue-router'
import translate from '../components/Translate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'translate',
      component: translate
    },
  ]
})

export default router
