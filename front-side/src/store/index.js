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
    token: null,
  },

  getters: {
    isLogin(state) {
      return state.token? true : false
    },
  },

  mutations: {
    GET_MOVIE(state, Movies) {
      state.Movies = Movies
    },

    SAVE_TOKEN(state, token) {
      state.token = token
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
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
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
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
