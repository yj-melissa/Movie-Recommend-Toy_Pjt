<template>
  <b-container class="mt-3 bv-example-row animate__animated animate__fadeInRight" >
    <b-row class="text-center my-3">
      <b-col>
        <label for="search">검색</label>
        <b-input-group id="search">
          <b-form-input v-model="keywordtemp" @keyup.enter="maketempsearch" type="text"></b-form-input>
          <b-input-group-append>
            <b-input-group-text>
              <b-icon icon="search"/>
            </b-input-group-text>
          </b-input-group-append>
        </b-input-group>
      </b-col>
    </b-row>
    
    <div v-if="isLoding==1">
      <b-card class="bg-dark text-white " title="검색 결과">
        <b-card-text>
          검색중...
        </b-card-text>
      </b-card>
    </div>
    <div v-else>
      <b-card class="bg-dark text-white " title="검색 결과">
        <b-card-text v-if="Movie" >
          <b-list-group>
            <b-list-group-item class="bg-secondary text-left" v-for="movie in changeMovie" :key="movie.id">
              <router-link class="decorate-none" :to="{ name: 'MovieDetailView', params: { movieid : movie.id } }"> {{movie.title}} </router-link>
            </b-list-group-item>
          </b-list-group>
        </b-card-text>
        <b-card-text v-else id="box">
          <b-row class="mt-5">
            <b-col class="text-center mt-5">
              검색 결과가 없습니다...
            </b-col>
          </b-row>
        </b-card-text>
      </b-card>
    </div>
    
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
    name : 'SearchView',
    data(){
        return{
          isLoding : 0,
          Movie : [],
          keyword : null,
          keywordtemp : null,
        }
    },
    methods : {
        getSearch(){
          this.isLoding = 1
          const API_URL = process.env.VUE_APP_API_URL
          axios({
            method : 'get',
            url : `${API_URL}/api/v1/server/getsearch/`,
            params : {
                search : this.keyword
            },
          })
            .then((res)=>{
              console.log(res)
              this.Movie = res.data
              this.isLoding = 0
            })
            .catch((err)=> {
              console.log(err)
            })
          },
        makesearch(){
          this.keyword = this.$route.params.serchname
        },
        maketempsearch(){
          this.keyword = this.keywordtemp
          console.log(this.keyword)
        }
    },
    computed:{
        changeMovie(){
          return this.Movie
        },
        changekeword(){
          return this.keyword          
        }
    },
    created(){
        this.makesearch()
    },
    watch : {
      changekeword(){
        this.getSearch()
      }
    }
}
</script>
<style scoped>
a{text-decoration:none; 
  color: white
}
#box{
  min-height: 300px;
}
</style>