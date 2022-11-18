<template>
  <carousel :per-page="1" class="bannaer_list"
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
      <img :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" alt="">
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
  props : {
    Movies : Array,
  },
  methods:{
  },
}
</script>
