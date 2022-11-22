<template>
  <div class="container row mt-3 animate__animated animate__fadeInRight" style="margin:0 auto">
    <b-container class="bv-example-row">
      <div id="card" class="card">
        <b-row class="card-header mt-3" >
          <b-col cols="12" class="text-center">
            <h2 class="p-0">{{ article?.title }}</h2>
          </b-col>
        </b-row>
        <b-row>
          <b-col class="text-left pl-4 pt-3" align-self="center" cols="3">작성자 : {{ article?.user.nickname }}</b-col>
          <b-col cols="9" align-self="center" class="text-right pr-4 pt-3" v-show="isAuthor">
            <b-button-group>
              <router-link :to="{name : 'ArticleCreateView', params: { articleid:article?.id } } "><b-button variant="info">수정</b-button></router-link>
              <b-button @click="articleDelete" variant="danger">삭제</b-button>
            </b-button-group>
          </b-col>
        </b-row>
        <div class="p-1 card-body">
          <b-row align-v="center">
            <b-col>
              <div class="card-text text-left ml-2 p-3" id="content">
                {{ article?.content }}
              </div>
            </b-col>
          </b-row>
        </div>

        <div class="card-footer container p-0 text-center">
          <b-row align-v="center">
            <b-col cols="11">
              <textarea 
                id="textarea-rows"
                placeholder="댓글을 입력해주세요"
                rows="3"
                v-model="newComment"
                class="w-100 p-2 m-2"
                @keyup.enter="createComment"
              >
              </textarea>
            </b-col>
            <b-col class="pr-4 text-left"><button @click="createComment" class="px-2 py-4  btn btn-outline-secondary">입력</button></b-col>
          </b-row>
          <ul class="list-group list-group-flush p-0 m-0 text-left">
            <ArticleDetailComments
              v-for="comment in comments"
              :key="comment.id"
              :comment="comment"
              @comment-update="getCommentData"
              class="list-group-item bg-transparent"
            />
          </ul>
        </div>
      </div>
    </b-container>
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
#card{
  min-height: 600px;
}
#content{
  min-height: 200px;
}
</style>