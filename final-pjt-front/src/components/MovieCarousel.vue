<template>
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
