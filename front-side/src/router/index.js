import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RecommendView from '@/views/RecommendView.vue'
import CommunityView from '@/views/CommunityView.vue'
import LoginView from '@/views/LoginView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },  
  {
    path: '/detail',
    name: 'MovieDetailView',
    component: MovieDetailView
  },  
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },  

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
