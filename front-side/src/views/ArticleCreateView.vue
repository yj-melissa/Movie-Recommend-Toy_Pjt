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
    <b-col><router-link :to="{name : 'CommunityView'} "><button @click="createArticle" >작성하기</button></router-link> </b-col>
  </b-row>
</b-container>
</template>

<script>
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
        const data = {
            title : this.title,
            content : this.content
        }
        this.$store.dispatch('createArticle',data)
    }
  },

}
</script>

<style>

</style>