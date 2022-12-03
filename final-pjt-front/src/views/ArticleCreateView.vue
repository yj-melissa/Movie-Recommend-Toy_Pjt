<template>
  <b-container class="mt-3 bv-example-row animate__animated animate__fadeInRight">
    <div class="card">
      <b-row class="card-header mt-3" >
        <b-col cols="12" class="text-center">
          <h4 class="b-col" v-if="isEdit">글 수정하기</h4>
          <h4 class="b-col" v-else>글 작성하기</h4>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="mx-1 my-2">
          <b-input-group size="lg" prepend="제목">
              <b-form-input v-model="title" placearea="title"></b-form-input>
          </b-input-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="m-1">
          <b-form-textarea
              id="textarea-rows"
              placeholder="내용을 입력하세요"
              rows="25"
              v-model="content"
          ></b-form-textarea>
        </b-col>
      </b-row>
      <b-row align-v="center" class="my-2 mx-1 text-right">
        <b-col></b-col>
        <b-col></b-col>
        <b-col>
          <b-button @click="editArticle" v-if="isEdit">수정하기</b-button>
          <b-button @click="createArticle" v-else>작성하기</b-button>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script>
import axios from 'axios'

export default {
  name : 'ArticleCreateView',
  data(){
    return{
        title : null,
        content : null,
        isEdit : false,
    }
  },
  methods: {
    createArticle(){
      const title = this.title
      const content = this.content
      const API_URL = process.env.VUE_APP_API_URL
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if(!content) {
        alert('내용을 입력해주세요')
        return
      } else {
        axios({
          method : 'post',
          url: `${API_URL}/api/v1/community/getarticles/`,
          headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
          data :{
            title, content
          },
        })
          .then((res)=> {
            // console.log(res)
            const articleid = res.data.id
            this.$router.push({ name: 'ArticleDetailView', params: { articleid: articleid } }) 
          })
          .catch(()=>{
            alert('로그인해주세요')
            return
          })
      }
    },
    getArticleData() {
      const articleId = this.$route.params.articleid
      if (articleId) {
        const API_URL = process.env.VUE_APP_API_URL
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/community/${articleId}/`,
          headers: {
            Authorization: `Bearer ${this.$store.getters.getToken}`
          }
        })
          .then((res) => {
            const data = res.data
            this.title = data.title
            this.content = data.content
            this.isEdit = true
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    editArticle() {
      const title = this.title
      const content = this.content
      const API_URL = process.env.VUE_APP_API_URL
      const articleId = this.$route.params.articleid
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if(!content) {
        alert('내용을 입력해주세요')
        return
      } else {
        axios({
          method : 'put',
          url: `${API_URL}/api/v1/community/${articleId}/`,
          headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
          data :{
            title, content
          },
        })
          .then(()=> {
            this.$router.push({ name: 'ArticleDetailView', params: { articleid: articleId } }) 
          })
          .catch((err)=>{
            console.log(err)
          })
      }
    }
  },
  created() {
    if (this.$route.params) {
      this.getArticleData()
    }
  }
}
</script>

<style>

</style>