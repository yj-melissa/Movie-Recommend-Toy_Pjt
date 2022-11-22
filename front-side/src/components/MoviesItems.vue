<template>
  <div class="home m-0 animate__animated animate__fadeInRight">
    <div id="select">
      <p> <b-button @click="select1" variant="outline-light">인기순</b-button> <b-button @click="select2" variant="outline-light">평점순</b-button> <b-button @click="select3" variant="outline-light">최신순</b-button> </p>
    </div>
    <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
            <div>
              <b-card-group class="my-2" deck v-for="movie in this.MovieData.slice(0,3)" :key="movie.number" :movie="movie">
                <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
                <b-card bg-variant="dark" text-variant="white" :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
                </b-card>
                </router-link>
              </b-card-group>
            </div>
        </b-col>
        <b-col>
          <div>
            <b-card-group class="my-2" deck v-for="movie in MovieData.slice(3,6)" :key="movie.number" :movie="movie">
              <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
              <b-card bg-variant="dark" text-variant="white" :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
              </b-card>
              </router-link>
            </b-card-group>
          </div>
        </b-col>
        <b-col>
          <div>
            <b-card-group class="my-2" deck v-for="movie in this.MovieData.slice(6,9)" :key="movie.number" :movie="movie">
              <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
              <b-card bg-variant="dark" text-variant="white" :title="movie.title" :img-src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" img-alt="Image" img-top>
              </b-card>
              </router-link>
            </b-card-group>
          </div>
        </b-col>
      </b-row>
    </b-container>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import _ from 'lodash'

export default {
  name: 'MoviesItems',
  props: {
    Movies : Array,
  },
  data(){
    return {
      MovieData : null,
      selected : null,
    }
  },
  methods: {
    getMovieData(){
      this.MovieData = _.cloneDeep(this.Movies)
    },
    selectOption(){
      const value = this.selected
      const Data = this.MovieData
      if(value == 2){
        Data.sort(function(a,b){
        return b.vote_average - a.vote_average  
        });
      } 
      else if(value == 3){
        Data.sort(function(a,b){
          let a_num = Number(a.release_date.replace(/-/g,''))
          let b_num = Number(b.release_date.replace(/-/g,''))
          return b_num - a_num
        })
      }
      else{
        Data.sort(function(a,b){
          return b.popularity - a.popularity
        })
      }
    },
    getMovies(){
      console.log(this.Movies)
      this.MovieData = this.Movies
    },
    select1(){
      this.selected = 1
    },
    select2(){
      this.selected = 2
    },
    select3(){
      this.selected = 3
    }
  },
  computed: {
    changeMovie(){
      return this.Movies
    },
    changevalue(){
      return this.selected
    }
  },
  watch : {
    changeMovie(val) {
      this.getMovieData(val)
    },
    changevalue(){
      this.selectOption()
    }
    
  },
  created(){
    this.getMovieData()
  }
}
</script>
<style scoped>
#select{
  font-size: 20px;
  color: beige;
}

</style>