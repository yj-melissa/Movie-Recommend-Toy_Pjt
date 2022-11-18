<template>
  <div>
    <b-container class="bv-example-row my-4">
      <b-row class="text-left">
        <b-col cols="12">
          <b-card :header="article?.title" style="height: 600px">
            <b-card-text>
              {{ article?.content }}
            </b-card-text>
            <ArticleDetailComments
              v-for="comment in article?.comment_set"
              :key="comment.id"
              :comment="comment"
              class="bg-secondary"
            />
            <template #footer>
              <b-form-textarea
                id="textarea-rows"
                placeholder="댓글을 입력해주세요"
                rows="4"
                v-model="newComment"
              >
              </b-form-textarea>
              <div class="text-right my-2">
                <button @click="createComment">입력</button>
              </div>
            </template>
          </b-card>
        </b-col>
      </b-row>
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
    }
  },
  computed: {
    // getArticle(){
    //     return this.$store.getters.getArticle
    // }
  },
  methods: {
    getArticleData() {
      const articleId = this.$route.params.articleid
      // this.$store.dispatch('getArticleDetail', articleId)
      const API_URL = `${process.env.VUE_APP_API_URL}`
      axios({
        method: "get",
        url: `${API_URL}/api/v1/community/${articleId}/`,
      })
        .then((res) => {
          const data = res.request.response
          const jsonData = JSON.parse(data)
          this.article = jsonData
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment() {
      const Article = this.article
      // User = 'admin',
      const Content = this.newComment
      if (!Content) {
        alert("댓글을 입력해주세요")
        return
      } else {
        const data = {
          Article: Article,
          // User : 'admin',
          Content: Content,
        }
        this.article = this.$store.dispatch("createComment", data)
        this.getArticleData()
        this.newComment=null
      }
    },
  },
  created() {
    this.getArticleData()
  },
}
</script>

<style>
</style>