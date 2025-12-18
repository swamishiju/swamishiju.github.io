import { createWebHashHistory, createRouter } from 'vue-router'

import HomePage from './Home/HomePage.vue'
import AboutPage from './About/AboutPage.vue'
import BlogHomePage from './Blog/BlogPage.vue'
import BlogViewPage from './Blog/BlogViewPage.vue'
import ProjectPage from './Projects/ProjectPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/about', component: AboutPage },
  { path: '/blog/:id', component: BlogViewPage },
  { path: '/blog', component: BlogHomePage },
  { path: '/projects', component: ProjectPage },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
