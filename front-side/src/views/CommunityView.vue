<template>
  <b-container class="bv-example-row">
    <b-row class="text-right">
      <b-col></b-col>
      <b-col cols="10">
        <button > <router-link :to="{name : 'ArticleCreateView'} ">글 쓰기</router-link> </button>
      </b-col>
      <b-col></b-col>
    </b-row>
    <b-row class="text-left">
      <b-col></b-col>
      <b-col cols="10">
        <b-list-group v-for="articles in getArticlesList" :key="articles.x" :articles="articles">
          <router-link :to="{name : 'ArticleDetailView', params:{articleid : articles.id} }"><b-list-group-item>제목 : {{ articles.title}}  내용 : {{ articles.content }}</b-list-group-item></router-link>
        </b-list-group>
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>
<script>
// @ is an alias to /src
export default {
  name: 'CommunityView',
  components: {
  },
  methods : {
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  },
  computed : {
    getArticlesList(){
      return this.$store.state.Articles
    }
  },
  created(){
    return this.getArticles()
  }
}
</script>
