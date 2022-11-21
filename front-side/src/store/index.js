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
    MovieDetail : null,
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
      state.AlgoMovieList = Movies
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
    },

    GET_ARTICLE_DATA(state, data) {
      state.article = data
    },
  }, 

  actions: {
    getMovie(context){
      console.log(`${API_URL}/api/v1/server/getmovie/`)
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/getmovie/`,
        headers: {
          Authorization: `Bearer ${context.getters.getToken}`
        }
      })
        .then((res)=>{
          // console.log(res.data)
          const Movies =res.data.slice(0,30)
          Movies.sort(function(a,b){
            let a_num = Number(a.release_date.replace(/-/g,''))
            let b_num = Number(b.release_date.replace(/-/g,''))
            return b_num - a_num
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
        .then(() => {
        })
        .catch(() => {
        })
        context.commit('LOGOUT')
    },
    saveUserInfo(context, data) {
      console.log(data)
      context.commit('SAVE_USER_INFO', data)
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
        },
        headers: {
          Authorization: `Bearer ${context.getters.getToken}`
        }
      })
        .then((res) => {
          const data = res.data
          context.commit('GET_REVIEW',data)
        })
        .catch((err)=> {
          alert('로그인해주세요')
          console.log(err)
        })
    },
    getReview(context){
      axios({
        method : 'GET',
        url : `${API_URL}/api/v1/server/getreview/`,
        headers: {
          Authorization: `Bearer ${context.getters.getToken}`
        }
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
