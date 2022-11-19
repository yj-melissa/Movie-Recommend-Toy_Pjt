<template>
  <div class="container row mt-3" style="margin:100 auto">
    <div class="card col-8 p-0 row justify-content-center text-left" style="margin:0 auto">
      <h4 class="card-header py-3">
        {{ article?.title }}
      </h4>
      <div class="card-body">
        <p class="card-text py-3">
          {{ article?.content }}
        </p>
      </div>
      <div class="card-footer container p-0 text-center">
        <ul class="list-group list-group-flush p-0 m-0 text-left">
          <ArticleDetailComments
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
            class="list-group-item bg-transparent"
          />
        </ul>
        <textarea 
          id="textarea-rows"
          placeholder="댓글을 입력해주세요"
          rows="4"
          v-model="newComment"
          class="justify-content-center col-11 mt-3"
        >
        </textarea>
        <div class="text-right my-2">
          <button @click="createComment" class="btn btn-outline-secondary mr-4">입력</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import ArticleDetailComments from "@/components/ArticleDetailComments"

export default {
  name: "ArticleDetailView",
  components: {
    ArticleDetailComments,
  },
  data() {
    return {
      article: null,
      newComment : null,
      comments: [],
    }
  },
  computed: {
  },
  methods: {
    getArticleData() {
      const articleId = this.$route.params.articleid
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${articleId}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCommentData() {
      const articleId = this.$route.params.articleid
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${articleId}/comments/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment() {
      const article = this.article
      // User = 'admin',
      const content = this.newComment
      if (!content) {
        alert("댓글을 입력해주세요")
        return
      } else {
        axios({
          method : 'post',
          url : `${process.env.VUE_APP_API_URL}/api/v1/community/${article.id}/createcomment/`,
          data : {
            content : content
          }
        })
          .then((res)=> {
            const data = res.data
            console.log(data)
            this.getCommentData()
            this.newComment=null
          })
          .catch((err)=> {
            console.log(err)
          })
      }
    },
  },
  created() {
    this.getArticleData()
    this.getCommentData()
  },
}
</script>

<style>

</style>