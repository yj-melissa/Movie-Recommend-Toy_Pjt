<template>
  <div>
    <h2>{{ nickname }}님의 프로필</h2>
    <h2>아이디: {{ profile.email }}</h2>
    <h2>{{ profile.nickname }}님이 작성한 글</h2>
    <ul v-for="article in profile.article_set" :key="article.x">
        <router-link :to="{ name: 'ArticleDetailView', params: { articleid : article.id } }">
          {{ article.title }}
        </router-link>
    </ul>
    <h2>{{ profile.nickname }}님이 작성한 댓글</h2>
    <ul v-for="comment in profile.comment_set" :key="comment.x">
        <router-link :to="{ name: 'ArticleDetailView', params: { articleid : comment.article } }">
          {{ comment.content }}
        </router-link>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "ProfileView",
  data() {
    return {
      nickname: null,
      profile: [],
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getUser() {
      if (this.isLogin) {
        const user = this.$store.getters.getUser
        this.nickname = user.nickname
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'LoginView' })
      }
    },
    getProfile() {
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/user/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          // console.log(res)
          this.profile = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created(){
    this.getUser()
    this.getProfile()
  }
}
</script>

<style>
</style>