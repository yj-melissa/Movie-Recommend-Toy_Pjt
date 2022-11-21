<template>
  <div class="TextAnime1">
    <b-container class="bv-example-row"  >
      <b-row>
        <b-col class="my-5">
          <p
            v-for="(t, index) in text"
            :key="index"
            class="item"
            :style="{animationDelay: index*100+'ms'}"
            v-text="t"
          />
          <b-card v-if="this.QuestionCount == 0" border-variant="dark" header="시작하기" align="center">
            <b-card-text>
              <div>
                <img class="w-75" src="/spaceship.png" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="select2" > 시작하기 </b-list-group-item>
              </b-list-group>
            </b-card-text>
          </b-card>
          <b-card v-else-if="this.QuestionCount < 11" border-variant="dark" :header="this.QuestonList[getNumber].Question" align="center">
            <b-card-text>
              <div v-if="this.QuestonList[getNumber].ImgUrl" class="my-2">
                <img :src="this.QuestonList[getNumber].ImgUrl" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="select1" > 네 </b-list-group-item>
                <b-list-group-item @click="select2" > 모르겠습니다 </b-list-group-item>
                <b-list-group-item @click="select3" > 아니오 </b-list-group-item>
                <b-progress :value="this.QuestionCount/10*100" variant="danger" :animated="true" class="mt-3"></b-progress>
                <p> {{this.QuestionCount}} / 10</p>
              </b-list-group>
            </b-card-text>
          </b-card>
          <b-card v-else border-variant="dark" header="혹시 이 영화인가요?" align="center">
            <b-card-text>
              <div>
                <img :src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+this.FirstMovie.poster_path" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="reset" > 다시하기 </b-list-group-item>
              </b-list-group>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col align-self="center"><img src="https://cdn0.iconfinder.com/data/icons/streamline-emoji-1/48/178-man-astronaut-2-512.png" alt=""></b-col>
      </b-row>
      <b-row>
        <b-col v-if="this.QuestionCount==0" >
          <p
            v-for="(t, index) in text2"
            :key="index"
            class="item"
            :style="{animationDelay: index*100+'ms'}"
            v-text="t"
          />
        </b-col>
        <b-col>

        </b-col>
      </b-row>
      <b-row v-if="this.QuestionCount==11">
        <div v-for="movie of this.AnoterMovie" :key="movie.index">
          <span></span>
        </div>
        <div>
        <b-carousel
          id="carousel-1"
          v-model="slide"
          :interval="4000"
          controls
          indicators
          background="#ababab"
          img-width="1024"
          img-height="480"
          style="text-shadow: 1px 1px 2px #333;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >
          <!-- Text slides with image -->
          <b-carousel-slide>
          <b-card-group>
            <b-card :img-src="'https://www.themoviedb.org/t/p/w300_and_h450_bestv2/'+movie.poster_path" img-alt="Image" img-top v-for="movie of this.AnoterMovie" :key="movie.index">
            </b-card>
          </b-card-group>

          </b-carousel-slide>
        </b-carousel>

        <p class="mt-4">
          Slide #: {{ slide }}<br>
          Sliding: {{ sliding }}
        </p>
      </div>
      </b-row>
    </b-container>
    
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      text: '좋아하는 영화를 하나 생각하세요',
      text2: '생각하셨나요?',
      RecommendList : null,
      FirstMovie : this.$store.state.Movies[0],
      QuestionCount : 0,
      QuestionNumber : 0,
      AnoterMovie : null,
      QuestonList : [
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.$store.state.AlgoMovieList[0].actors[0].profile_path}`,
          Question : `'${this.$store.state.Movies[0].actors[0].name}'이(가) 출연한 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.Movies[0].genre_ids[0]}' 장르의 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.Movies[0].release_date.split('-',1)}'년에 개봉한 영화인가요?`
        }
      ]
    }
  },
  name: 'RecommendView',
  methods : {
    getRandomNumber(){
      this.QuestionNumber = Math.floor(Math.random()*3)
    },

    reset(){
      this.QuestionCount = 0
      this.MovieDataList = this.$store.state.Movies
    },

    changeQuestion(){
      this.QuestonList = [
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.FirstMovie.actors[0].profile_path}`,
          Question : `'${this.FirstMovie.actors[0].name}'이(가) 출연한 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.FirstMovie.genre_ids[0]}' 장르의 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.FirstMovie.release_date.split('-',1)}'년에 개봉한 영화인가요?`
        }
      ]
    },

    select1(){
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      if(!this.RecommendList){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/server/${movieId}/${this.QuestionNumber}/1/sortmovie/`,
        })
          .then((res) => {
            this.RecommendList = res.data
            this.FirstMovie = res.data[0]
            this.QuestionCount += 1
            console.log(this.RecommendList)
            console.log(this.FirstMovie)
          })
          .catch((err) => {
            console.log(err)
          })
      } else{
        
        const MovieList = this.RecommendList
        
        if(this.QuestionNumber == 0){
          const Actor = this.FirstMovie.actors[0].name
          const NewList = []
          for(const Movie of MovieList){
            for(const MovieActorList of Movie.actors){
              if(Actor == MovieActorList.name){
                NewList.push(Movie)
              } 
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1

        }else if(this.QuestionNumber==1){
          const Genre = this.FirstMovie.genre_ids[0]
          const NewList = []
          for(const Movie of MovieList){
            let flag = 0
            for(const genre of Movie.genre_ids){
              if(genre == Genre){
                flag = 1
              } 
            }
            if(flag==1){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1

        }else if(this.QuestionNumber==2){
            const Release_date = Number(this.FirstMovie.release_date.split('-',1))
            const NewList = []
            for(const Movie of MovieList){
              if(Number(Movie.release_date.split('-',1)) == Release_date){
                NewList.push(Movie)
              }
            }
            this.RecommendList = NewList
            this.FirstMovie = NewList[0]
            console.log(this.FirstMovie)
            this.QuestionCount += 1
          }
        }
    },
    select2(){
      this.QuestionCount += 1
      console.log(this.QuestionCount)
    },
    select3(){
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      if(!this.RecommendList){
        axios({
          method: 'GET',
          url: `${API_URL}/api/v1/server/${movieId}/${this.QuestionNumber}/2/sortmovie/`,
        })
          .then((res) => {
            this.RecommendList = res.data
            this.FirstMovie = res.data[0]
            this.QuestionCount += 1
            console.log(this.FirstMovie)
            console.log(this.RecommendList)
          })
          .catch((err) => {
            console.log(err)
          })
  
      } else{
        const MovieList = this.RecommendList
        if(this.QuestionNumber == 0){
          const Actor = this.FirstMovie.actors[0].name
          const NewList = []
          for(const Movie of MovieList){
            let flag = 0
            for(const MovieActorList of Movie.actors){
              if(Actor == MovieActorList.name){
                flag = 1
              } 
            }
            if(flag == 0){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          console.log(this.FirstMovie)
          this.QuestionCount += 1

        }else if(this.QuestionNumber==1){
          const Genre = this.FirstMovie.genre_ids[0]
          const NewList = []
          for(const Movie of MovieList){
            let flag = 0
            for(const genre of Movie.genre_ids){
              if(genre == Genre){
                flag = 1
              } 
            }
            if(flag==0){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          console.log(this.FirstMovie)
          this.QuestionCount += 1

        }else if(this.QuestionNumber==2){
            const Release_date = Number(this.FirstMovie.release_date.split('-',1))
            const NewList = []
            for(const Movie of MovieList){
              if(Number(Movie.release_date.split('-',1)) != Release_date){
                NewList.push(Movie)
              }
            }
            this.RecommendList = NewList
            this.FirstMovie = NewList[0]
            console.log(this.FirstMovie)
            console.log(this.RecommendList)
            this.QuestionCount += 1
          }
        }
    },

    getAnoterMovie(){
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      console.log('또다른 영화는')
      axios({
          method: 'get',
          url: `${API_URL}/api/v1/server/${movieId}/anothermovie/`,
        })
          .then((res) => {
            const AnotherMovied = res.data
            AnotherMovied.sort(function(a,b){
              return b.popularity - a.popularity
            })
            this.AnoterMovie = AnotherMovied.slice(0,5)
          })
          .catch((err) => {
            console.log(err)
          })
    }

    
  },
  created(){
    this.getRandomNumber()
    this.changeQuestion()
  },
  computed: {
    changeCount(){
      return this.QuestionCount
    },
    getNumber(){
      return this.QuestionNumber
    }
  },
  watch : {
    QuestionCount: function(newValue){
      if(newValue == 11){
        this.getAnoterMovie()
      }
    },
    changeCount(){
      this.getRandomNumber()
      this.changeQuestion()
    },
    
    
  }
}

</script>

<style scoped>
@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 2rem;
  animation: text-in .8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
  color: #FAF9D9;
}
</style>
