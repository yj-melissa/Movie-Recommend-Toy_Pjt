import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Movies : [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIE(state,Movies){
      state.Movies = Movies
    },
  }, 
  actions: {
    getMovie(context){
      axios({
        method : 'get',
        url : 'https://api.themoviedb.org/3/movie/popular?api_key=81d72b8b58e4b26b26aae316e0bbad5c&language=ko-KR&page=1' 	
      })
        .then((res)=>{
          console.log(res.data)
          const Movies =res.data.results
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
