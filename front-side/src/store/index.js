import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = `${process.env.VUE_APP_API_URL}`

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],

  state: {
    Movies: [],
    DefaultMovies : [],
    token: null,
    userName: null,
    Articles : [],
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    getToken(state) {
      return state.token
    },
    getMovies(state){
      return state.Movies
    },
    getUserName(state) {
      return state.userName
    },
  },

  mutations: {
    GET_MOVIE(state, Movies) {
      state.Movies = Movies
      state.DefaultMovies = Movies
    },

    SAVE_USER_INFO(state, payload) {      
      const userInfo = payload.config.data
      const jsonUserInfo = JSON.parse(userInfo)
      state.token = payload.data.key
      state.userName = jsonUserInfo.username
      this.$router.push({ name: 'HomeView' })
    },
    
    LOGOUT(state) {
      state.token = null
      state.userName = null
      this.$router.push({ name: 'HomeView' })
    },

    GET_ARTICLES(state, Articels){
      state.Articles = Articels
    },

    CREATE_ARTICLES(state, Articels){
      state.Articles = Articels
    },
  }, 

  actions: {
    getMovie(context){
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/getmovie`
      })
        .then((res)=>{
          // console.log(res.data)
          const Movies =res.data
          context.commit('GET_MOVIE',Movies)
        })
        .catch((error)=> {
          console.log(error)
        })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_USER_INFO', res)
        })
        .catch((err) => {
          // const errMessage = err.response.request.responseText 
          const errMessage = err.response.request.response
          const jsonErrMessage = JSON.parse(errMessage)
          for (const [key, value] of Object.entries(jsonErrMessage)) {
            alert(`${key}: ${value}`)
          }
        })
    },
    logout(context) {
      const token = context.getters.getToken
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/logout/`,
        data: {
          key: token,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('LOGOUT', res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const email = payload.email
      const nickname = payload.nickname

      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: {
          username, password1, password2, email, nickname
        }
      })
        .then(res => {
          context.commit('SAVE_USER_INFO', res)
        })
        .catch(err => {
          const errMessage = err.response.request.response
          const jsonErrMessage = JSON.parse(errMessage)
          for (const [key, value] of Object.entries(jsonErrMessage)) {
            alert(`${key}: ${value}`)
          }
        })
    },
    getArticles(context){
      axios({
        method : 'get',
        url: `${API_URL}/api/v1/community/getarticles/`
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createArticle(context,payload){
      const title = payload.title
      const content = payload.content
      axios({
        method : 'post',
        url: `${API_URL}/api/v1/community/getarticles/`,
        data :{
          title, content
        }
      })
        .then((res)=> {
          const data = res.data
          context.commit('CREATE_ARTICLES', data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    createComment(context, data){
      const Article = data.Article
      // const User = data.User
      const Content = data.Content
      axios({
        method : 'post',
        url : `${API_URL}/api/v1/community/${Article.id}/createcomment/`,
        data : {
          // Article,
          // User,
          content: Content
        },
      })
        .then((res)=> {
          const data = res.data
          console.log(data)
        })
        .catch((err)=> {
          console.log(err)
          console.log(context)
        })
    },
    getDetail(context,movieid){
      axios({
        method: 'GET',
        url : `https://api.themoviedb.org/3/movie/${movieid}?api_key=${process.env.VUE_APP_APIKEY}&language=ko-KR`
      })
        .then((res)=> {
          console.log(res.data)
        })
        .catch((err)=>{
          console.log(err)
          console.log(context)
        })
    },
  },
  modules: {
  }
})
