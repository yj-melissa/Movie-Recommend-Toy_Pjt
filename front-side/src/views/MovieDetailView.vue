<template>
  <!-- <div class="">
    <img :src="imgSrc" alt="">
    <h1>{{ title }}</h1>
    <p>{{ overview }}</p>
    <iframe width="640" height="360" 
      :src="videoSrc" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
    <div>한줄평+별점</div>
    <div>한줄평 작성</div>
    <button>좋아요</button>
  </div> -->
  
  <b-container class="bv-example-row my-4 " id="grid" >
      <b-row class="text-left">
        <b-col cols="6" class="px-0" >
          <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+changeMovie.poster_path" alt="">
        </b-col>
        <b-col cols="6" class="px-0" >
          <h1>{{ changeMovie.title }}</h1>
          <p>{{ changeMovie.overview }}</p>
          <p> 평점 : {{ changeMovie.vote_average}}</p>
          <p> 개봉일자 : {{ changeMovie.release_date}}</p>
          <p> 상영시간 : {{ changeMovie.runtime}} 분 </p>
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
  </b-container>
</template>

<script>
// import axios from 'axios'
// @ is an alias to /src
export default {
  name: 'MovieDetailView',
  data() {
    return {
      Moviedata : [],
      Star : null,
      newComment : null
    }
  },
  methods: {
    getDetail(data){
      this.$store.dispatch('getDetail',data)
    },
    // 영화 트레일러 가져오기 (axios, youtubeAPI 이용)
    // youTube key 암호화 처리 필요함!
    // getVideo() {
    //   const baseUrl = 'https://www.youtube.com/watch?v='
    //   axios({
    //     method: 'get',
    //     url: 'https://www.googleapis.com/youtube/v3/search',
    //     params: {
    //       part: 'snippet',
    //       // key: 'YOUTUBE API KEY',
    //       q: this.title,
    //       type: 'video',
    //       videoDuration: 'short',
    //       regionCode: 'KR',
    //       maxResults: '1',
    //     },
    //   })
    //     .then(res => {
    //       const videoId = res.data.items[0].id.videoId
    //       this.videoSrc = baseUrl + videoId + '&output=embed'
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
    createComment(){
      this.$store.dispatch('createMovieComment',this.newComment)
      this.newComment = null
    }
  },
  created() {
    this.getDetail(this.$route.params.movieid)
  },
  computed: {
    changeMovie(){
      return this.$store.state.MovieDetail
    },
  },
}
</script>
