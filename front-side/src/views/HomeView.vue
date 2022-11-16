<template>
  <div class="home">
    <MovieCarousel
      :Movies = getMovieList
    />
    <MoviesItems
     v-for="movie in getMovieList" :key="movie.number" :movie="movie"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCarousel from '@/components/MovieCarousel'
import MoviesItems from '@/components/MoviesItems'

export default {
  name: 'HomeView',
  data(){
    return {
      Movies : null
    }
  },
  components: {
    MovieCarousel,
    MoviesItems
  },
  methods : {
    getMovie(){
      this.$store.dispatch('getMovie')
    }
  },
  created(){
    return this.getMovie()
  },
  computed: {
    getMovieList(){
      return this.$store.state.Movies
    }
  }
}
</script>
