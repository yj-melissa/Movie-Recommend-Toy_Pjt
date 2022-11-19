<template>
  <div class="home">
    <h1>LOGIN</h1>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="email" class="form-label">이메일: </label><br>
        <input type="text" id="email" v-model.trim="email">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">PASSWORD</label><br>
        <input type="password" id="password" v-model.trim="password">
      </div>
      <button type="submit" class="btn btn-primary btn-sm m-2">LOGIN</button>
      <router-link :to="{ name: 'SignUpView' }" class="btn btn-outline-primary btn-sm m-2">SIGNUP</router-link>
    </form>
    {{ user }}
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
export default {
  name: 'LoginView',
  data() {
    return {
      email: null,
      password: null,
      user: null,
    }
  },
  methods: {
    login() {
      const API_URL = 'http://127.0.0.1:8000'
      const email = this.email
      const password = this.password
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/accounts/login/`,
        data: {
          email, password
        }
      })
        .then((res) => {
          const data = {
            accessToken: res.data.access_token,
            refreshToken: res.data.refresh_token,
            user: {
              pk: res.data.user.pk,
              nickname: res.data.user.nickname
            }
          }
          localStorage.setItem('access_token', res.data.access_token)
          localStorage.setItem('refresh_token', res.data.refresh_token)
          this.$store.dispatch('saveUserInfo', data)
          this.$router.push({ name: 'ProfileView' })
        })
        .catch((err) => {
          const errMessage = err.response.request.response
          alert(errMessage)
        })
    },
  }
}
</script>