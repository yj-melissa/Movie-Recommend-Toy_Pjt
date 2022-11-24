<template>
  <b-container class="animate__animated animate__backInRight bv-example-row">
    <div id="con"></div>
    <b-row align-v="center" class="mt-4">
    <b-col cols="3"></b-col>
    <b-col cols="6">
    <b-card title="SIGN UP" >
      <b-card-text>
        <form @submit.prevent="signUp">
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
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="input-2"> Password : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="input-2"
                v-model.trim="password1"
                type="password"
                placeholder="Enter Password"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="input-3"> Password Check : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="input-3"
                v-model.trim="password2"
                type="password"
                placeholder="Enter Password once again"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="input-4"> Nickname : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="input-4"
                v-model.trim="nickname"
                type="text"
                placeholder="Enter Your Nickname"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-button type="submit" class="mx-2" variant="outline-success">Make Your Account Now! </b-button>
            </b-col>
          </b-row>
        </form>
      </b-card-text>
    </b-card>
    </b-col>
    </b-row>
  </b-container>
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
      const API_URL = process.env.VUE_APP_API_URL
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
          alert(`${data.user.nickname}님을 환영합니다!`)
          this.$router.push({ name: 'HomeView' })
        })
        .catch((err) => {
          const errMessage = err.response.request.response
          console.log(errMessage)
          alert(errMessage)
          // const jsonErrMessage = JSON.parse(errMessage)
          // for (const [key, value] of Object.entries(jsonErrMessage)) {
          //   alert(`${key}: ${value}`)
          // }
        })
    },
  }
}
</script>

<style>
#con{
  min-height: 100px;
}
</style>