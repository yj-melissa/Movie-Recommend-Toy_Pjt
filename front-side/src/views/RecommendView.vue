<template>
  <div class="TextAnime1 animate__animated animate__fadeInRight">
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
          <b-card v-if="this.isloading == 1" border-variant="dark" header="" align="center">
            <b-card-text>
              <div>
                <img class="animate__animated animate__backOutUp w-75" src="/spaceship.png" alt="">
              </div>
              <b-list-group>
                <b-list-group-item> 결과를 찾으러 갑니다... </b-list-group-item>
              </b-list-group>
            </b-card-text>
          </b-card>
          <b-card v-else-if="this.isloadingWait == 1" border-variant="dark" header="" align="center">
            <b-card-text>
              <div>
                <img class="animate__animated animate__backOutUp w-75" src="/spaceship.png" alt="">
              </div>
              <b-list-group>
                <b-list-group-item> 결과를 찾으러 갑니다... </b-list-group-item>
              </b-list-group>
            </b-card-text>
          </b-card>
          <b-card v-else-if="this.QuestionCount == 0" border-variant="dark" header="시작하기" align="center">
            <b-card-text>
              <div>
                <img class="w-75" src="/spaceship.png" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="select2" > 시작하기 </b-list-group-item>
              </b-list-group>
            </b-card-text>
          </b-card>
          <b-card v-else-if="this.QuestionCount == 1" border-variant="dark" :header="this.QuestonList[getNumber].Question" align="center">
            <b-card-text>
              <div v-if="this.QuestonList[getNumber].ImgUrl" class="my-2">
                <img :src="this.QuestonList[getNumber].ImgUrl" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="select1" > 네 </b-list-group-item>
                <b-list-group-item @click="select3" > 아니오 </b-list-group-item>
                <b-progress :value="this.QuestionCount/10*100" variant="danger" :animated="true" class="mt-3"></b-progress>
                <p> {{this.QuestionCount}} / 10</p>
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
          <b-card v-else-if="this.QuestionCount == 11" border-variant="dark" header="혹시 이 영화인가요?" align="center">
            <b-card-text>
              <div class="my-4">
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
      <b-row v-if="this.AnotherMovie" >
        <b-row>
          <b-col cols="12" id="m-title" class="text-center">
            <b-badge href="#" variant="dark">비슷한 장르, 배우가 출연한 영화 </b-badge>
          </b-col>
        </b-row>
        <carousel-3d :disable3d="true" :space="365" :width="300" :height="450" :clickable="false" :controls-visible="true">
          <slide v-for="(movie,i) in this.AnotherMovie" :index="i" :key="i" :movie="movie">
            <template slot-scope="{ index, isCurrent, leftIndex, rightIndex}">
              <router-link :to="{name : 'MovieDetailView', params:{movieid : movie.id}}">
              <img :data-index="index" 
              class="h-100 w-100" :class="{ current: isCurrent, onLeft: (leftIndex>=0), onRight: (rightIndex >=0) }" :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2/'+movie.poster_path" >
              </router-link>
            </template>
          </slide>
        </carousel-3d>
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
      isloading : 0,
      RecommendList : null,
      FirstMovie : this.$store.state.Movies[0],
      QuestionCount : 0,
      isloadingWait : 0,
      QuestionNumber : 0,
      AnotherMovie : null,
      QuestonList : [
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.$store.state.Movies[0].actors[0].profile_path}`,
          Question : `'${this.$store.state.Movies[0].actors[0].name}'이(가) 출연한 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.Movies[0].genre_ids[0]}' 장르의 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.Movies[0].release_date.split('-',1)}'년에 개봉한 영화인가요?`
        },
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.$store.state.Movies[0].director.profile_path}`,
          Question : `영화의 감독이 '${this.$store.state.Movies[0].director.name}' 인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.Movies[0].release_date.substr(0,3)}0'년대 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : '한국 영화인가요?'
        }
      ]
    }
  },
  name: 'RecommendView',
  methods : {
    getRandomNumber(){
      this.QuestionNumber = Math.floor(Math.random()*6)
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
        },
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.FirstMovie.director.profile_path}`,
          Question : `영화의 감독이 '${this.FirstMovie.director.name}' 인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.FirstMovie.release_date.substr(0,3)}0'년대 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : '한국 영화인가요?'
        }
      ]
    },
    select1(){
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      if(!this.RecommendList){
        this.isloadingWait = 1
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/server/${movieId}/${this.QuestionNumber}/1/sortmovie/`,
        })
          .then((res) => {
            this.RecommendList = res.data
            console.log(this.RecommendList)
            this.FirstMovie = res.data[0]
            this.QuestionCount += 1
            this.isloadingWait = 0
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
        }else if(this.QuestionNumber==3){
          const Director = this.FirstMovie.director.name
          const NewList = []
          for(const Movie of MovieList){
            if(Movie.director.name == Director){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1
        }else if(this.QuestionNumber==4){
          const decade = Number(this.FirstMovie.release_date.substr(0,3)+'0')
          const NewList = []
          for(const Movie of MovieList){
            if(Number(Movie.release_date.substr(0,3)+'0') == decade ){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1

        }else if(this.QuestionNumber==5){
          const language = "ko"
          const NewList = []
          for(const Movie of MovieList){
            if(Movie.original_language == language){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1
        }
      }
      
    },
    select2(){
      this.QuestionCount += 1
    },
    select3(){
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      if(!this.RecommendList){
        this.isloadingWait = 1
        axios({
          method: 'GET',
          url: `${API_URL}/api/v1/server/${movieId}/${this.QuestionNumber}/2/sortmovie/`,
        })
          .then((res) => {
            this.RecommendList = res.data
            this.FirstMovie = res.data[0]
            this.QuestionCount += 1
            this.isloadingWait = 0
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
            this.QuestionCount += 1
        }else if(this.QuestionNumber==3){
          const Director = this.FirstMovie.director.name
          const NewList = []
          for(const Movie of MovieList){
            if(Movie.director.name != Director){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1
        }else if(this.QuestionNumber==4){
          const decade = Number(this.FirstMovie.release_date.substr(0,3)+'0')
          const NewList = []
          for(const Movie of MovieList){
            if(Number(Movie.release_date.substr(0,3)+'0') != decade ){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1
        }else if(this.QuestionNumber==5){
          const language = "ko"
          const NewList = []
          for(const Movie of MovieList){
            if(Movie.original_language != language){
              NewList.push(Movie)
            }
          }
          this.RecommendList = NewList
          this.FirstMovie = NewList[0]
          this.QuestionCount += 1
        }
      }
    },
    getAnoterMovie(){
      this.isloading = 1
      const movieId = this.FirstMovie.id
      const API_URL = process.env.VUE_APP_API_URL
      axios({
          method: 'get',
          url: `${API_URL}/api/v1/server/${movieId}/anothermovie/`,
        })
          .then((res) => {
            const AnotherMovied = res.data
            AnotherMovied.sort(function(a,b){
              return b.popularity - a.popularity
            })
            console.log(AnotherMovied)
            this.AnotherMovie = AnotherMovied.slice(0,10)
            this.isloading = 0
          })
          .catch((err) => {
            console.log(err)
          })
    },
    
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
.animate__animated.animate__fadeInRight {
  --animate-duration: 1.5s;
}
.animate__animated.animate__backOutUp {
  --animate-duration: 5s;
}

#m-title{
  color: bisque;
  font-size: 25px;
}
</style>