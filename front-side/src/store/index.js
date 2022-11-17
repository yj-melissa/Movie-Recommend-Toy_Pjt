import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '@/router'
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
    token: null,
    userName: null,
  },

  getters: {
    isLogin(state) {
      return state.token? true : false
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

    SAVE_USER_INFO(state, data) {      
      const userInfo = data.config.data
      const jsonUserInfo = JSON.parse(userInfo)
      state.token = data.token
      state.userName = jsonUserInfo.username
      // router.push({name: 'HomeView'})
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
          console.log(err)
        })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const email = payload.email
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: {
          username, password1, password2, email,
        }
      })
        .then(res => {
          context.commit('SAVE_USER_INFO', res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
