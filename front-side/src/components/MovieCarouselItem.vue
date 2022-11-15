<template>
  <div class="carousel-item active">
    <img :src="Url" alt="">
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'MovieCarouselItem',
  data(){
    return {
        Url : `https://image.tmdb.org/t/p/w600_and_h900_bestv2/${this.Movie.poster_path}`
    }
  },
  props : {
    Movie : Object
  },
  components: {
  },
  methods: {
    getMovieDetail(){
        axios({
        method : 'get',
        url : 'https://openapi.naver.com/v1/search/movie.json',
        params : {
            query : '007',
            // display : 5
        },
        headers: {
            'X-Naver-Client-Id': 'tAu9L8IOuiLh__cEIP8A' , 
            'X-Naver-Client-Secret': 'xx6_RkQrbx'
        }
        })
          .then((res)=> {
            console.log(res)
          })
          .catch((error)=> {
            console.log(error)
          })
    }
  },
  created(){
    return this.getMovieDetail()
  }
}
</script>
