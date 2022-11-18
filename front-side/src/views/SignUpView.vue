<template>
  <div>
    <h1>SIGN UP</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">아이디 : </label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password1">비밀번호 : </label>
        <input type="password" id="password1" v-model="password1">
      </div>
      <div>
        <label for="password2">비밀번호 재확인: </label>
        <input type="password" id="password2" v-model="password2">
      </div>
      <div>
        <label for="email">이메일 : </label>
        <input type="email" id="email" v-model="email">
      </div>
      <div>
        <label for="nickname">닉네임 : </label>
        <input type="text" id="nickname" v-model="nickname">
      </div>
      <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
      nickname: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      const nickname = this.nickname

      const payload = {
        username, password1, password2, email, nickname
      }

      this.$store.dispatch('signUp', payload)
    }
  },
}
</script>

<style>
</style>