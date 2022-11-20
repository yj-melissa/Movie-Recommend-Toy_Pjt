<template>
  <b-container class="bv-example-row">
  <b-row class='my-4'>
    <b-col>글 작성하기</b-col>
  </b-row>
  <b-row>
    <b-input-group size="lg" prepend="제목">
        <b-form-input v-model="title"></b-form-input>
    </b-input-group>
  </b-row>
  <b-row class="mt-4">
    <b-form-textarea
        id="textarea-rows"
        placeholder="Tall textarea"
        rows="8"
        v-model="content"
    ></b-form-textarea>
  </b-row>
  <b-row class="mt-4 text-right">
    <b-col></b-col>
    <b-col></b-col>
    <b-col><button @click="createArticle">작성하기</button></b-col>
  </b-row>
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
          .then(()=> {
            alert(`글 등록 성공`)
            this.$router.push({ name: 'CommunityView' }) 
          })
          .catch((err)=>{
            console.log(err)
          })
      }
    },
  },

}
</script>

<style>

</style>