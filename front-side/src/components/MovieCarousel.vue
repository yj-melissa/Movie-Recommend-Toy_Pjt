<template>
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item" v-for="(movie,idx,index) in Movies" :key="index" :class="{ active: idx==0 }">
        <img :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" alt="" class="img-fluid">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  data(){
    return{
      Url1 : null,
      Url2 : null,
      Url3 : null,
      Url4 : null,
      Url5 : null 
    }
  },
  name: 'MovieCarousel',
  props : {
    Movies : Array
  },

  components: {
    
  },
}
</script>
