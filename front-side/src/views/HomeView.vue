<template>
  <div class="home">
    <MovieCarousel
      :Movies = getMovieList
    />
    <div>
      <label for="fiterselect">정렬하기</label>
      <select name="fiterselect" id="fiterselect" @change="getOption">
        <option value="1">인기순</option>
        <option value="2">평점순</option>
        <option value="3">최신순</option>
      </select>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <div>
            <b-card-group deck v-for="movie in this.Movies.slice(0,3)" :key="movie.number" :movie="movie">
              <b-card :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
              </b-card>
            </b-card-group>
          </div>
        </b-col>
        <b-col>
          <div>
            <b-card-group deck v-for="movie in this.Movies.slice(3,6)" :key="movie.number" :movie="movie">
              <b-card :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
              </b-card>
            </b-card-group>
          </div>
        </b-col>
        <b-col>
          <div>
            <b-card-group deck v-for="movie in this.Movies.slice(6,9)" :key="movie.number" :movie="movie">
              <b-card :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
              </b-card>
            </b-card-group>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCarousel from '@/components/MovieCarousel'

export default {
  name: 'HomeView',
  data(){
    return {
      Movies : null,
      Movieoption : 1
    }
  },
  components: {
    MovieCarousel,
  },
  methods : {
    getMovie(){
      this.$store.dispatch('getMovie')
    },
    getOption(event){
      this.Movies = this.$store.state.Movies
      if (event.target.value == 2){
        this.Movies.sort(function(a,b){
        return b.vote_average - a.vote_average
      });
      } 
    },
    getDefaultMovie(){
      this.Movies = this.$store.state.Movies
    }
  },
  created(){
    this.getMovie()
    return this.getDefaultMovie()
  },
  computed: {
    getMovieList(){
      return this.$store.state.Movies
    }
  }
}
</script>
