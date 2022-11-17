import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Movies : [],
    DefaultMovies : []
  },
  getters: {
    getMovies(state){
      return state.Movies
    }
  },
  mutations: {
    GET_MOVIE(state,Movies){
      state.Movies = Movies
      state.DefaultMovies = Movies
    },
  }, 
  actions: {
    getMovie(context){
      axios({
        method : 'get',
        url : 'http://127.0.0.1:8000/api/v1/server/getmovie'
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
  },
  modules: {
  }
})
