<template>
  <b-container class="bv-example-row">
    <b-row class="text-right">
      <b-col></b-col>
      <b-col cols="10">
        <button> <router-link :to="{name : 'ArticleCreateView'} ">글 쓰기</router-link> </button>
      </b-col>
      <b-col></b-col>
    </b-row>
    <b-row class="text-left">
      <b-col></b-col>
      <b-col cols="10">
        <b-list-group v-for="article in articles" :key="article.x" :articles="article">
          <router-link :to="{name : 'ArticleDetailView', params:{articleid : article.id} }">
            <b-list-group-item>제목 : {{ article.title }}</b-list-group-item>
          </router-link>
        </b-list-group>
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>
<script>
import axios from 'axios'
export default {
  name: 'CommunityView',
  data() {
    return {
      articles: [],
    }
  },
  methods : {
    getArticles(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method : 'get',
        url: `${API_URL}/api/v1/community/getarticles/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          // console.log(res)
          this.articles = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created(){
    return this.getArticles()
  }
}
</script>
