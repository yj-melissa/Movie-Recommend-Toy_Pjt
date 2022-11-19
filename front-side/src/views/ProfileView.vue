<template>
  <div>
    <h2>{{ pk }}</h2>
    <h2>{{ nickname }}</h2>
  </div>
</template>

<script>
export default {
  name: "ProfileView",
  data() {
    return {
      pk: null,
      nickname: null,
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
        this.pk = user.pk
        this.nickname = user.nickname
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'LoginView' })
      }
    }
  },
  created(){
    this.getUser()
  }
}
</script>

<style>
</style>