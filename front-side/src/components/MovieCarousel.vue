<template>
  <carousel :per-page="1" class="animate__animated animate__bounceInRight my-5"
    paginationActiveColor ='#e01a31'
    paginationColor ="#999"
    :paginatioinPadding=3
    style="height:100%; width:100%"
    :autoplay = "true"
    :autoplayTimeout = "4000"
    :loop = "true"
    >
    <slide v-for="movie of Movies.slice(0, 4)" :key="movie.seq" class="slide_item">
      <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
        <img :class="{'animate__animated animate__backOutUp': value == '1' }" @click="changevalue" :src="'https://image.tmdb.org/t/p/w300_and_h450_bestv2/'+movie.poster_path" alt="">
      </router-link>
    </slide>
  </carousel>
</template>

<script>
// @ is an alias to /src
import { Carousel,Slide } from 'vue-carousel'

export default {
  components:{
    Carousel,Slide
  },
  name: 'MovieCarousel',
  data(){
    return{
      value : 0
    }
  },
  props : {
    Movies : Array,
  },
  methods:{
    changevalue(){
      this.value=1
    }
  },
}
</script>
