<template>
  <b-container class="animate__animated animate__fadeInRight bv-example-row my-4" id="grid" :style="{ backgroundColor: '#000000'}" >
      <b-row class="text-left">
        <b-col cols="6" class="px-0 text-center p-5" >
          <img v-if="changeMovie" :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+changeMovie.poster_path" alt="">
        </b-col>
        <b-col v-if="changeMovie" cols="6" class="p-5" id="box" >
          <b-row><h1 class="white-text">{{ changeMovie.title }}</h1></b-row>
          <b-row><p class="white-text" >{{ changeMovie.overview }}</p></b-row>
          <b-row>
            <b-col>
              <span class="white-text"> 평점 : {{ changeMovie.vote_average}} </span>
            </b-col>
            <b-col> 
              <span class="text-right">
                <p @click="like" v-if="this.value == 0 " class="h3" > Pick <b-icon-lightning-fill variant="danger"></b-icon-lightning-fill></p>
                <p @click="like" v-else-if="this.value == 1" class="h3" > Drop <b-icon-lightning-fill variant="dark"></b-icon-lightning-fill></p>
              </span>
            </b-col>
          </b-row>
          
          <p class="white-text"> 개봉일자 : {{ changeMovie.release_date}}</p>
          <p class="white-text"> <span>장르 : </span><span v-for="genre of changeMovie.genre_ids" :key="genre.id" :genre="genre"> {{genre}} </span></p>
          <p class="white-text"> 감독 : {{ changeMovie.director.name}} </p>
          
        </b-col>
      </b-row>
      <b-row class="mb-2">
        <b-col class="text-center text-white" cols="4" >출연진</b-col>
        <b-col >
        </b-col>
        <b-col></b-col>
      </b-row>
        
      <b-row>
        <b-col clos="2" ></b-col>
        <b-col v-if="changeMovie" class="text-center" cols="9">
          <b-list-group horizontal>
            <b-list-group-item class=" mx-1 bg-dark" v-for="actor of changeMovie.actors.slice(0,5)" :key="actor.id">
              <b-card
                :img-src="`https://www.themoviedb.org/t/p/w138_and_h175_face/${actor.profile_path}`"
                img-top
                style="max-width: 120px;"
                class="mb-2 bg-secondary"
              >
                <b-card-text class="text-white bg-secondary">
                  {{actor.name}}
                </b-card-text>
              </b-card>
            </b-list-group-item>
          </b-list-group>
        </b-col>
        <b-col></b-col>
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
      <b-row class="text-center" align-v="center">
        <b-col cols='8'></b-col>
        <b-col cols='1' id="score">
          <span> 평점 : </span>
        </b-col>
        <b-col>
          <b-form-rating v-model="score" variant="warning" class="mb-2"
            show-value
            show-value-max
            precision="0"
            size="lg"></b-form-rating>
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
        <b-col>
        <b-pagination
          pills
          class="mt-4"
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          size="sm"
          align="center"
          aria-controls="commentlist"
        ></b-pagination>

        <b-list-group class="w-100 text-left px-4 mb-5 ">
          <b-list-group-item>
            <b-row>
              <b-col class="text-center" cols="2">작성자</b-col>
              <b-col class="text-center" cols="8">한줄평</b-col>
              <b-col class="text-center" cols="2">평점</b-col>
            </b-row>
          </b-list-group-item>
          <div v-if="this.ReviewList.length>0">
          <b-list-group-item id='commentlist' :per-page="perPage" :current-page="currentPage" v-for="review in itemForList" :key="review.number" :review="review">
            <b-container>
              <b-row align-v="center">
                <b-col cols='2'>{{review.user.nickname}}</b-col>
                <b-col cols='8' class="px-4">
                  <span>{{review.content}}</span><button class="ml-2 text-danger" v-if="user.pk == review.user.id" @click="commentDelete(`${review.id}`,$event)">x</button>
                </b-col>
                <b-col cols='2' class="text-center py-2 px-0">
                  <span
                  v-for="index in 5"
                  :key="index"
                  class="text-right">
                    <span class="m-0 p-0" v-if="index < review.score">🌕</span>
                    <span class="m-0 p-0" v-if="index >= review.score">🌑</span>
                  </span>
                </b-col>
              </b-row>
            </b-container>
          </b-list-group-item>
          </div>
        </b-list-group>
        </b-col>
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
      user : this.$store.state.user ,
      MovieDetail : null,
      Moviedata : [],
      Star : null,
      newComment : null,
      ReviewList : [],
      videoId : null,
      score: 3,
      value : 0,
      isReview : 0,

      currentPage : 1,
      perPage : 4,

      spare : null
    }
  },
  methods: {
    getDetail(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/server/${this.$route.params.movieid}/getdetail`,
      })
        .then((res)=>{
          this.MovieDetail = res.data
        })
        .catch((err)=> {
          console.log(err)
        })
    },


    getReview(){
      this.$store.dispatch('getReview')
    },
    
    createComment(){
      if(this.isReview == 1){
        alert('이미 한줄평을 남겼습니다.')
        this.newComment = null
      }else{
        const data = {
          movie_id : this.$route.params.movieid,
          content : this.newComment,
          score : this.score+1,
          user_id : this.$store.getters.getUser.pk
        }
        this.$store.dispatch('createMovieReview',data)
        this.newComment = null
      }
    },
    getReviewList(){
      const List = []
      const ReviewList = this.$store.state.ReviewList
      for(const review of ReviewList){
        if(review.movie == this.$route.params.movieid){
          List.push(review)
        }
      }
      this.ReviewList = List
      for(const MovieReview of this.ReviewList){
        if (MovieReview.user.id == this.$store.state.user.pk){
          this.isReview = 1
        }
      }
      this.Moviedata = this.$store.state.MovieDetail
    },
    getVedio(){
      // console.log(`https://www.googleapis.com/youtube/v3/search?key=${process.env.VUE_APP_YOUTUBE_APIKEY}&part=snippet&type=video&q=${this.$store.state.MovieDetail.title}공식예고편`)
      axios({
        method : 'get',
        url : `https://www.googleapis.com/youtube/v3/search?key=${process.env.VUE_APP_YOUTUBE_API_KEY}&part=snippet&type=video&q=${this.MovieDetail.title}공식예고편`
      })
        .then((res)=>{
          this.videoId = res.data.items[0].id.videoId
        })
        .catch((err)=> {
          console.log(err)
        })
    },
    check(index) {
      this.score = index + 1;
    },

    like(){
      const API_URL = process.env.VUE_APP_API_URL
      if(this.value == 1){
        axios({
        method : 'get',
        url: `${API_URL}/api/v1/server/${this.$route.params.movieid}/1/likes`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          this.spare = res.data
          this.value = 0
        })
        .catch((err)=>{
          console.log(err)
        })
      } else {
        axios({
        method : 'get',
        url: `${API_URL}/api/v1/server/${this.$route.params.movieid}/0/likes`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          this.spare = res.data
          this.value = 1
        })
        .catch((err)=>{
          console.log(err)
        })
      }
      
    },
    checkLike(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
      method : 'get',
      url: `${API_URL}/api/v1/server/${this.$route.params.movieid}/likelist`,
      headers: {
        Authorization: `Bearer ${this.$store.getters.getToken}`
      }
      })
        .then((res) => {
          for(const user of res.data.like_users){
            if(user == this.$store.state.user.pk){
              this.value = 1
            }
          }
        })
        .catch((err)=>{
          console.log(err)
        })
    },

    commentDelete(event) {
      const CommentId = event
      axios({
        method : 'delete',
        url : `${process.env.VUE_APP_API_URL}/api/v1/server/${CommentId}/deletereview/`,
        headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
      })
        .then((res) => {
          const List = []
          for(const review of res.data){
            if(review.movie == this.$route.params.movieid){
              List.push(review)
            }
          }
          this.ReviewList = List
          this.$store.dispatch('changeReview',List)
          this.isReview = 0
        })
        .catch((err) => {
          console.log(err)
        })
    }

  },
  created() {
    this.getReviewList()
    this.getDetail()
    this.checkLike()
  },
  computed: {
    changeMovie(){
      return this.MovieDetail
    },
    changeReview(){
      return this.$store.state.ReviewList
    },
    getUrl(){
      return `https://www.youtube.com/embed/${this.videoId}?autoplay=1&mute=1 `
    },
    rows(){
      return this.ReviewList.length
    },
    itemForList(){
      return this.ReviewList.slice((this.currentPage - 1) * this.perPage,this.currentPage * this.perPage);
    }
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
#score{
  color: lightgray;
}
.animate__animated.animate__fadeInRight {
  --animate-duration: 0.5s;
}
</style>