<template>
  <b-container class="bv-example-row my-4" id="grid" :style="{ backgroundColor: '#000000'}" >
    <!-- :style="{ backgroundImage: 'url(https://www.themoviedb.org/t/p/w600_and_h900_bestv2/' + changeMovie.backdrop_path + ')' }" -->
      <b-row class="text-left">
        <b-col cols="6" class="px-0 text-center p-5" >
          <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+changeMovie.poster_path" alt="">
        </b-col>
        <b-col cols="6" class="p-5" id="box" >
          <h1 class="white-text">{{ changeMovie.title }}</h1>
          <p class="white-text" >{{ changeMovie.overview }}</p>
          <p class="white-text" > 평점 : {{ changeMovie.vote_average}}</p>
          <p class="white-text"> 개봉일자 : {{ changeMovie.release_date}}</p>
          <p class="white-text"> 상영시간 : {{ changeMovie.runtime}} 분 </p>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols='12' class="my-4">
          <div v-if="this.videoId" id="video">
              <iframe :src="getUrl" width="900" height="400" class="responsive-iframe"
              frameborder="0" 
              >
              </iframe>
          </div>
        </b-col>
      </b-row>
      <b-row class="my-4">
        <b-col>
          <b-form-textarea
              id="textarea-rows"
              placeholder="댓글을 입력해주세요"
              rows="4"
              v-model="newComment"
              @keyup.enter="createComment"
          ></b-form-textarea>
          <div class="text-right my-2">
              <button @click="createComment">입력</button>
          </div>
        </b-col>
      </b-row>
      <b-row>
        <b-list-group class="w-100 text-left px-4 mb-5">
          <b-list-group-item v-for="review in this.ReviewList" :key="review.number" :review="review">{{review.content}}</b-list-group-item>
        </b-list-group>
      </b-row>
  </b-container>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
export default {
  name: 'MovieDetailView',
  data() {
    return {
      Moviedata : [],
      Star : null,
      newComment : null,
      ReviewList : [],
      videoId : null,
      playerVars: {
        autoplay: 1
      }
    }
  },
  methods: {
    getDetail(data){
      this.$store.dispatch('getDetail',data)
    },
    getReview(){
      this.$store.dispatch('getReview')
    },
    
    createComment(){
      const data = {
        movie_id : this.$route.params.movieid,
        content : this.newComment
      }
      this.$store.dispatch('createMovieReview',data)
      this.newComment = null
    },
    getReviewList(){
      const List = []
      const ReviewList = this.$store.state.ReviewList
      for(const review of ReviewList ){
        if(review.movie == this.$route.params.movieid){
          List.push(review)
        }
      }
      this.ReviewList = List
      this.Moviedata = this.$store.state.MovieDetail
      console.log(this.Moviedata)
    },
    getVedio(){
      axios({
        method : 'get',
        url : `https://www.googleapis.com/youtube/v3/search?key=${process.env.VUE_APP_YOUTUBE_APIKEY}&part=snippet&type=video&q=${this.$store.state.MovieDetail.title}공식예고편`
      })
        .then((res)=>{
          this.videoId = res.data.items[0].id.videoId
        })
        .catch((err)=> {
          console.log(err)
        })
    }
  },
  created() {
    this.getReviewList()
    this.getDetail(this.$route.params.movieid)
  },
  computed: {
    changeMovie(){
      return this.$store.state.MovieDetail
    },
    changeReview(){
      return this.$store.state.ReviewList
    },
    getUrl(){
        return `https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1 `
    },
  },
  watch : {
    changeReview() {
      this.getReviewList()
    },
    changeMovie(){
      this.getVedio()
    }
  }
}
</script>
<style>
#box{
  color: lightgray;
}
</style>