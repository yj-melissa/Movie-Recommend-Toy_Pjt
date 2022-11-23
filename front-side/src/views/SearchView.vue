<template>
  <b-container class="mt-3 bv-example-row animate__animated animate__fadeInRight" >
    <b-card class="bg-dark text-white " title="검색 결과">
    <b-card-text v-if="Movie.length>0" >
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
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
    name : 'SearchView',
    data(){
        return{
            Movie : []
        }
    },
    methods : {
        getSearch(){
            const API_URL = process.env.VUE_APP_API_URL
            axios({
                method : 'get',
                url : `${API_URL}/api/v1/server/getsearch/`,
                params : {
                    search : this.$route.params.serchname
                },
            })
              .then((res)=>{
                console.log(res)
                this.Movie = res.data
              })
              .catch((err)=> {
                console.log(err)
              })
            },
        clean(){
            this.Movie = []
        }
    },
    computed:{
        changeMovie(){
            return this.Movie
        }
    },
    created(){
        this.getSearch()
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