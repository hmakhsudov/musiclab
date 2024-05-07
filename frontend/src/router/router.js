import { createRouter, createWebHistory } from 'vue-router'
import WelcomeView from '@/views/WelcomeView.vue'
import RegisterFirstView from '@/views/RegisterFirstView.vue'
import RegisterSecondView from '@/views/RegisterSecondView.vue'
import Blog from '@/components/Blog.vue'
import TestsView from '@/views/TestsView.vue'
import TestPageView from '@/views/TestPageView.vue'  // Подставьте путь к компоненту, отображающему страницу теста
import LoginView from '@/views/LoginView.vue'  // Подставьте путь к компоненту, отображающему страницу теста

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: WelcomeView,
    },
    {
      path: '/registerfirst/',
      name: 'registerfirst',
      component: RegisterFirstView,
    },
    {
      path: '/registersecond/',
      name: 'registersecond',
      component: RegisterSecondView,
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/blog/',
      name: 'blog',
      component: Blog,
    },
    {
      path: '/tests/',
      name: 'tests',
      component: TestsView,
    },
    {
      path: '/test/:id/question/:questionIndex',  // Маршрут с динамическим параметром id для передачи ID теста
      name: 'TestPage',
      component: TestPageView
    },
  ]
})
