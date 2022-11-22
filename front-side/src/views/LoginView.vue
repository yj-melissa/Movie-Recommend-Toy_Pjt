<template>
  <b-container class="animate__animated animate__bounceInDown bv-example-row">
    <div id="con"></div>
    <b-row align-v="center" class="mt-4">
    <b-col cols="3"></b-col>
    <b-col cols="6">
    <b-card title="LOGIN" >
      <b-card-text>
        <form @submit.prevent="login">
          <b-row class="mt-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="input-1"> E-mail : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="input-1"
                v-model.trim="email"
                type="email"
                placeholder="Enter email"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-3" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="input-2"> Password : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="input-2"
                v-model.trim="password"
                type="password"
                placeholder="Enter Password"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-button type="submit" class="mx-2" variant="outline-dark">LOGIN</b-button>
              <router-link :to="{ name: 'SignUpView' }"><b-button variant="outline-success">SIGN UP</b-button></router-link>
            </b-col>
          </b-row>
        </form>
      </b-card-text>
        
      
    </b-card>
    </b-col>
    <b-col></b-col>
    </b-row>
  </b-container>
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
          this.$router.push({ name: 'HomeView' })
        })
        .catch((err) => {
          const errMessage = err.response.request.response
          alert(errMessage)
        })
    },
  },
  created() {
    localStorage.clear()
  }
}
</script>

<style scoped>
#con{
  min-height: 250px;
}
</style>