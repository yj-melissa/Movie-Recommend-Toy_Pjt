import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],

  state: {
    Movies: [],
    DefaultMovies : [],
    MovieDetail : null,
    token: null,
    userName: null,
    Articles : [],
    ReviewList : [],
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
      // this.$router.push({ name: 'HomeView' })
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

    GET_DETAIL(state,data){
      state.MovieDetail = data
    },

    GET_REVIEW(state, data){
      state.ReviewList = data
    },

  }, 

  actions: {
    getMovie(context){
      console.log(`${API_URL}/api/v1/server/getmovie/`)
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/getmovie/`
      })
        .then((res)=>{
          // console.log(res.data)
          const Movies =res.data
          Movies.sort(function(a,b){
            return b.popularity - a.popularity
          })
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
          console.log('res')
          console.log(res)
          context.commit('SAVE_USER_INFO', res)
        })
        .catch(err => {
          console.log('err:')
          console.log(err)
          const errMessage = err.response.request.response
          const jsonErrMessage = JSON.parse(errMessage)
          alert(jsonErrMessage)
          // for (const [key, value] of Object.entries(jsonErrMessage)) {
          //   alert(`${key}: ${value}`)
          // }
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
    getArticleData(context, articleId) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/community/${articleId}/`,
      })
        .then((res) => {
          const data = res.request.response
          const jsonData = JSON.parse(data)
          // console.log(jsonData)
          context.commit('GET_ARTICLE_DATA', jsonData)
        })
        .catch((err) => {
          console.log(err)
        })
      },
    getDetail(context,movieid){
      axios({
        method: 'GET',
        url : `https://api.themoviedb.org/3/movie/${movieid}?api_key=${process.env.VUE_APP_APIKEY}&language=ko-KR`
      })
        .then((res)=> {
          const data = res.data
          context.commit('GET_DETAIL',data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    createMovieReview(context, data){
      console.log(data)
      const movieid = data.movie_id
      // const User = data.User
      const content = data.content
      axios({
        method : 'POST',
        url : `${API_URL}/api/v1/server/${movieid}/createreview/`,
        data : {
          content : content
        }
      })
        .then((res) => {
          const data = res.data
          context.commit('GET_REVIEW',data)
        })
        .catch((err)=> {
          console.log(err)
        })
    },
    getReview(context){
      axios({
        method : 'GET',
        url : `${API_URL}/api/v1/server/getreview/`
      })
        .then((res)=>{
          const data = res.data
          context.commit('GET_REVIEW',data)
        })
        .catch((err)=>{
          console.log(err)
        })
    },
  },
  modules: {
  }
})
