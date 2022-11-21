<template>
  <div v-if="isLoading" id="loading-page">
    <b-container class="bv-example-row">
      <b-row class="p-5"></b-row>
      <b-row class="p-5"></b-row>
      <b-row>
        <b-col cols='4'></b-col>
        <b-col cols='2'>
          <fade-images :delay="500" :width="200" :height="200"
            :images="images" />
        </b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
      <b-row class="p-5"></b-row>
      <b-row class="p-5"></b-row>
      <b-row class="p-3"></b-row>
      <b-row>
        <b-col>
          <div class="TextAnime1">
            <!-- <img class="w-25" src="/spaceship.png" alt=""> -->
            <p
              v-for="(t, index) in text"
              :key="index"
              class="item"
              :style="{animationDelay: index*100+'ms'}"
              v-text="t"
            />
          </div>
        </b-col>
      </b-row>
    </b-container>
      
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
import FadeImages from 'vue-fade-images'

export default {
  name: 'HomeView',
  data(){
    return {
      text : '로 딩 중 . . .',
      Movies_dafault : null,
      Movies_data : [],
      Movieoption : 1,
      isLoading : true,
      images: [
        {src: require("@/assets/spaceship.png")},
        {src: require("@/assets/spaceship2.png")},
        {src: require("@/assets/spaceship3.png")}
      ]
    }
  },
  components: {
    MovieCarousel,
    MoviesItems,
    FadeImages
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
  background:rgba(34,34,34,0.5);
  color : white;
  height: 100%;
}

#loading-page{
  color: azure;
  font-size: 25px;
}

@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 2rem;
  animation: text-in .8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
  color: #FAF9D9;
}
</style>