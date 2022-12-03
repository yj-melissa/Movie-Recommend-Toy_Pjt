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
    getRefresh(state) {
      return state.refreshToken
    }
  },

  mutations: {
    GET_MOVIE(state, data) {
      state.Movies = data
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

    CHANGE_REVIEW(state, List){
      state.ReviewList = List
    }
  }, 

  actions: {
    getMovie(context){
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/getmovie/`,
      })
        .then((res)=>{
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
      const movieid = data.movie_id
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
        .catch(()=>{
        })
    },
    
    changeReview(context, List){
      context.commit('CHANGE_REVIEW',List)
    }
  },
  modules: {
  }
})
