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
    Articles : [],
    ReviewList : [],
    accessToken : null,
    refreshToken: null,
    user: [],
  },

  getters: {
    getMovies(state){
      return state.Movies
    },
    getUser(state) {
      return state.user
    },
    isLogin(state) {
      return state.accessToken ? true : false
    },
    getToken(state) {
      return state.accessToken
    },
  },

  mutations: {
    GET_MOVIE(state, Movies) {
      state.Movies = Movies
      state.DefaultMovies = Movies
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

    SAVE_USER_INFO(state, data) {
      state.accessToken = data.accessToken
      state.refreshToken = data.refreshToken
      state.user = data.user
    },

    LOGOUT(state) {
      state.accessToken = null, 
      state.refreshToken = null, 
      state.user = []
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
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

    logout(context) {
      const token = context.getters.getToken
      // console.log(token)
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/logout/`,
        headers: {
          Authorization: `Bearer ${token}`,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('LOGOUT')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    saveUserInfo(context, data) {
      console.log(data)
      context.commit('SAVE_USER_INFO', data)
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
      const score = data.score
      axios({
        method : 'POST',
        url : `${API_URL}/api/v1/server/${movieid}/createreview/`,
        data : {
          content : content,
          score : score
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
