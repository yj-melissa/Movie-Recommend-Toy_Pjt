<template>
  <div class="container row mt-3" style="margin:0 auto">
    <div class="card col-12 p-0 row justify-content-center text-left" style="margin:0 auto">
      <h4 class="card-header py-3">
        {{ article?.title }}
      </h4>
      <div class="card-body">
        <p>작성자 : {{ article?.user.nickname }}</p>
        <p class="card-text py-3">
          {{ article?.content }}
        </p>
        <div v-show="isAuthor">
          <button> <router-link :to="{name : 'ArticleCreateView', params: { articleid:article?.id } } ">수정</router-link></button>
          <button @click="articleDelete">삭제</button>
        </div>
      </div>
      <div class="card-footer container p-0 text-center">
        <ul class="list-group list-group-flush p-0 m-0 text-left">
          <ArticleDetailComments
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
            @comment-update="getCommentData"
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
      isAuthor: false,
    }
  },
  methods: {
    getArticleData() {
      const articleId = this.$route.params.articleid
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${articleId}/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.article = res.data
          this.checkAuthor()
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
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkAuthor() {
      const user = this.$store.getters.getUser.pk
      const author = this.article.user.id
      if (user == author) {
        this.isAuthor = true
      }
    },
    createComment() {
      // User = 'admin',
      const articleId = this.$route.params.articleid
      const content = this.newComment
      if (!content) {
        alert("댓글을 입력해주세요")
        return
      } else {
        axios({
          method : 'post',
          url : `${process.env.VUE_APP_API_URL}/api/v1/community/${articleId}/createcomment/`,
          headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
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
    articleDelete() {
      const articleId = this.$route.params.articleid
      axios({
        method : 'delete',
        url : `${process.env.VUE_APP_API_URL}/api/v1/community/${articleId}/`,
        headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'CommunityView'})
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getArticleData()
    this.getCommentData()
  },
}
</script>

<style>

</style>