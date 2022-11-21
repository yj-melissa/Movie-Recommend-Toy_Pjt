import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RecommendView from '@/views/RecommendView.vue'
import CommunityView from '@/views/CommunityView.vue'
import LoginView from '@/views/LoginView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView'
import ArticleCreateView from '@/views/ArticleCreateView'
import ArticleDetailView from '@/views/ArticleDetailView'
import ProfileView from '@/views/ProfileView'
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
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },  
  {
    path: '/detail/:movieid',
    name: 'MovieDetailView',
    component: MovieDetailView
  },  
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },  
  {
    path: '/articlecreate',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },  
  {
    path: '/articleedit/:articleid',
    name: 'ArticleEditView',
    component: ArticleCreateView
  },
  {
    path: '/articledetail/:articleid',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
