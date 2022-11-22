<template>
  <!-- <carousel :per-page="1" class="animate__animated animate__bounceInRight my-5"
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
  </carousel> -->
  <carousel-3d :width="450" :height="600" :autoplay="true">
    <slide v-for="(movie,i) in this,Movies.slice(0,5)" :index="i" :key="i" :movie="movie">
      <template slot-scope="{ index, isCurrent, leftIndex, rightIndex}">
        <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
        <img :data-index="index" 
        class="h-100 w-100" :class="{ current: isCurrent, onLeft: (leftIndex>=0), onRight: (rightIndex >=0) }" :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" >
        </router-link>
      </template>
    </slide>
  </carousel-3d>
</template>

<script>
// @ is an alias to /src
// import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  components:{
    // Carousel3d,
    // Slide,
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
