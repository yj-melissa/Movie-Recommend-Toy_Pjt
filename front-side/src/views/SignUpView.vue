<template>
  <div>
    <h1>SIGN UP</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="email">이메일 : </label>
        <input type="email" id="email" v-model.trim="email">
      </div>
      <div>
        <label for="password1">비밀번호 : </label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>
      <div>
        <label for="password2">비밀번호 재확인: </label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>
      <div>
        <label for="nickname">닉네임 : </label>
        <input type="text" id="nickname" v-model.trim="nickname">
      </div>
      <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "SignUpView",
  data() {
    return {
      password1: null,
      password2: null,
      email: null,
      nickname: null,
    }
  },
  methods: {
    signUp() {
      const API_URL = 'http://127.0.0.1:8000'

      const email = this.email
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: {
          email, password1, password2, nickname
        }
      })
        .then((res) => {
          const data = res.data
          localStorage.setItem('access_token', data.access_token)
          localStorage.setItem('refresh_token', data.refresh_token)
          this.$store.dispatch('saveUserInfo', data.user)
          alert(`${data.user.nickname}님을 환영합니다!`)
          this.$router.push({ name: 'LoginView' })
        })
        .catch((err) => {
          const errMessage = err.response.request.response
          // console.log(errMessage)
          alert(errMessage)
          // const jsonErrMessage = JSON.parse(errMessage)
          // for (const [key, value] of Object.entries(jsonErrMessage)) {
          //   alert(`${key}: ${value}`)
          // }
        })
    }
  },
}
</script>

<style>
</style>