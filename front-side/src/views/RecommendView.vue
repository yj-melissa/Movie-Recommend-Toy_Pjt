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
          <b-card v-else-if="this.QuestionCount < 10" border-variant="dark" :header="this.QuestonList[getNumber].Question" align="center">
            <b-card-text>
              <div v-if="this.QuestonList[getNumber].ImgUrl" class="my-2">
                <img :src="this.QuestonList[getNumber].ImgUrl" alt="">
              </div>
              <b-list-group>
                <b-list-group-item @click="select1" > 네 </b-list-group-item>
                <b-list-group-item @click="select2" > 모르겠습니다 </b-list-group-item>
                <b-list-group-item @click="select3" > 아니오 </b-list-group-item>
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
        <b-col><img src="https://cdn0.iconfinder.com/data/icons/streamline-emoji-1/48/178-man-astronaut-2-512.png" alt=""></b-col>
      </b-row>
      <b-row>
        <b-col>
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
    </b-container>
    
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: '좋아하는 영화를 하나 생각하세요',
      text2: '생각하셨나요?',
      MovieDataList : this.$store.state.AlgoMovieList,
      FirstMovie : this.$store.state.AlgoMovieList[0],
      QuestionCount : 0,
      QuestionNumber : 0,
      QuestonList : [
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.$store.state.AlgoMovieList[0].actors[0].profile_path}`,
          Question : `'${this.$store.state.AlgoMovieList[0].actors[0].name}'이(가) 출연한 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.AlgoMovieList[0].genre_ids[0]}' 장르의 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.AlgoMovieList[0].release_date.split('-',1)}'년에 개봉한 영화인가요?`
        }
      ]
    }
  },
  name: 'RecommendView',
  methods : {
    getRandomNumber(){
      this.QuestionNumber = Math.floor(Math.random()*3)
      console.log(this.QuestionNumber)
    },
    select1(){
      const QuestionNumber = this.QuestionNumber
      const select = 1
      const MovieList = this.MovieDataList
      const Actor = this.FirstMovie.actors[0].name
      const Genre = this.FirstMovie.genre_ids[0]
      const release_date = this.FirstMovie.release_date.split('-',1)
      const data = {
        QuestionNumber,
        select,
        MovieList,
        Actor,
        Genre,
        release_date
      } 
      this.$store.dispatch('algo',data)
      this.QuestionCount += 1
      console.log(this.QuestionCount)
    },
    select2(){
      this.QuestionCount += 1
      console.log(this.QuestionCount)
    },
    select3(){
      const QuestionNumber = this.QuestionNumber
      const select = 2
      const MovieList = this.MovieDataList
      const Actor = this.FirstMovie.actors[0].name
      const Genre = this.FirstMovie.genre_ids[0]
      const release_date = this.FirstMovie.release_date.split('-',1)
      const data = {
        QuestionNumber,
        select,
        MovieList,
        Actor,
        Genre,
        release_date
      } 
      this.$store.dispatch('algo',data)
      this.QuestionCount += 1
      console.log(this.QuestionCount)
    },

    reset(){
      this.QuestionCount = 0
      this.MovieDataList = this.$store.state.Movies
    },

    getMovieList(){
      this.MovieDataList = this.$store.state.AlgoMovieList,
      this.FirstMovie = this.$store.state.AlgoMovieList[0],
      this.QuestonList = [
        {
          ImgUrl : `https://image.tmdb.org/t/p/w300_and_h450_bestv2/${this.$store.state.AlgoMovieList[0].actors[0].profile_path}`,
          Question : `'${this.$store.state.AlgoMovieList[0].actors[0].name}'이(가) 출연한 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.AlgoMovieList[0].genre_ids[0]}' 장르의 영화인가요?`
        },
        {
          ImgUrl : null,
          Question : `'${this.$store.state.AlgoMovieList[0].release_date.split('-',1)}'년에 개봉한 영화인가요?`
        }
      ]
      console.log(this.FirstMovie)
    },
  },
  created(){
    this.getRandomNumber()
    this.getMovieList()
  },
  computed: {
    changeMovie(){
      return this.$store.state.AlgoMovieList
    },
    changeCount(){
      return this.QuestionCount
    },
    getNumber(){
      return this.QuestionNumber
    }
  },
  watch : {
    changeCount(){
      this.getRandomNumber()
      this.getMovieList()
    }
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
