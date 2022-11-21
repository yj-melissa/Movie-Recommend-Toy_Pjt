<template>
  <div v-if="isLoading">
    <!-- <q-spinner-cube
    color = "primary"
    size = "5em"/> -->
    <p id="spinner-div"> 로딩중 </p>
  </div>
  <div v-else class="mt-3">
    <MovieCarousel
      :Movies = getMovieData
    />
    <MoviesItems
      :Movies = getMovieData
    />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCarousel from '@/components/MovieCarousel.vue'
import MoviesItems from '@/components/MoviesItems.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  data(){
    return {
      Movies_dafault : null,
      Movies_data : [],
      Movieoption : 1,
      isLoading : true,
    }
  },
  components: {
    MovieCarousel,
    MoviesItems
  },
  methods : {
    getMovie(){
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/getmovie/`
      })
        .then((res)=>{
          // console.log(res.data)
          const Movies =res.data
          // Movies.sort(function(a,b){
          //   let a_num = Number(a.release_date.replace(/-/g,''))
          //   let b_num = Number(b.release_date.replace(/-/g,''))
          //   return b_num - a_num
          // })
          Movies.sort(function(a,b){
            return b.popularity - a.popularity
          })
          this.Movies_data = Movies
          this.isLoading = false
        })
        .catch((error)=> {
          console.log(error)
        })
    },
    getReview(){
      this.$store.dispatch('getReview')
    }
  },
  created(){
    this.getReview() 
    return this.getMovie()
  },
  computed: {
    getMovieData(){
      return this.Movies_data
    },
    getDefaultMovies(){
      return this.$store.state.DefaultMovies
    },
  }
}
</script>
<style>
#spinner-div{
  background-color: aqua;
  color : white;
  height: 100%;
}
</style>