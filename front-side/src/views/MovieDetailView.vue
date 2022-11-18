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
  <b-container class="bv-example-row my-4">
      <b-row class="text-left">
          <b-col cols="6" class="px-0" >
            <img :src="imgSrc" alt="">
          </b-col>
          <b-col cols="6" class="px-0" >
            <h1>{{ title }}</h1>
            <p>{{ overview }}</p>

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
      title: null,
      overview: null,
      imgSrc: null,
      videoSrc: null,
    }
  },
  methods: {
    getDetail(){
      const movie = this.getMovie
      this.title = movie.title
      this.overview = movie.overview
      // poster url
      const baseUrl = 'https://image.tmdb.org/t/p/w300_and_h450_bestv2'
      const posterPath = movie.poster_path
      this.imgSrc = baseUrl + posterPath
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
  },
  computed: {
    getMovie(){
      return this.$store.state.Movies[0]
    },
  },
  created() {
    this.getDetail()
    this.getVideo()
  }
}
</script>
