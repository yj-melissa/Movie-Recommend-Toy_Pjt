<template>
  <div class="home">
    <MovieCarousel
      :Movies = getDefaultMovies
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

export default {
  name: 'HomeView',
  data(){
    return {
      Movies_dafault : null,
      Movies_data : null,
      Movieoption : 1
    }
  },
  components: {
    MovieCarousel,
    MoviesItems
  },
  methods : {
    getMovie(){
      this.$store.dispatch('getMovie')
    },
  },
  created(){ 
    return this.getMovie()
  },
  computed: {
    getMovieData(){
      return this.$store.state.Movies
    },
    getDefaultMovies(){
      return this.$store.state.DefaultMovies
    },
  }
}
</script>