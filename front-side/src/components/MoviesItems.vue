<template>
  <div class="home">
    <div>
      <label for="fiterselect">정렬하기</label>
      <select name="fiterselect" id="fiterselect" @change="selectOption">
        <option value="1">인기순</option>
        <option value="2">평점순</option>
        <option value="3">최신순</option>
      </select>
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
      MovieData : [],
    }
  },
  methods: {
    getMovieData(data){
      this.MovieData = _.cloneDeep(data)
    },
    selectOption(event){
      const value = event.target.value
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
    view(){
      console.log(this.$store.state.Movies)
    }
  },
  computed: {
    changeMovie(){
      return this.$store.state.Movies
    },
  },
  watch : {
    changeMovie(val) {
      this.getMovieData(val)
    }
  }
}
</script>
