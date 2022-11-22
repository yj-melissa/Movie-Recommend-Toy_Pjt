<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col class="text-center" cols='12'><h4 class="mt-4 ml-1">회원 정보 수정</h4></b-col>
    </b-row>
    <b-row>
      <b-col></b-col>
      <b-col cols="10">
        <b-row align-v="center" class="my-2">
          <b-col cols="2" class="px-0"><label class="m-0" for="nickname">닉네임 : </label></b-col>
          <b-col cols="9">
            <form v-if="editingNickname" @submit.prevent="editNickname">
              <b-row>
                <b-col class="px-0"><input type="text" id="nickname" v-model.trim="nickname"></b-col>
                <b-col class="px-0"><b-button size="sm" type="submit" value="editNickname">수정</b-button></b-col>
              </b-row>
            </form>
            <div v-else @click="editNickname">{{ current_nickname }}</div>
          </b-col>
        </b-row>
        <b-row class="my-2">
          <form @submit.prevent="editPassword">
            <div>
              <label for="password1">비밀번호 : </label>
              <input class="mx-2" type="password" id="password1" v-model.trim="password1" />
            </div>
            <div>
              <label for="password2"> 재 확 인 : </label>
              <input class="mx-3" type="password" id="password2" v-model.trim="password2" />
            </div>
            <b-button type="submit" value="editPassword">수정하기</b-button>
          </form>
        </b-row>
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios"

export default {
  name: "ProfileEditItem",
  data() {
    return {
      nickname: null,
      password1: null,
      password2: null,
      editingNickname: false,
      editingPassword: false,
    }
  },
  props: {
    current_nickname: String,
  },
  methods: {
    currentNickname() {
      this.nickname = this.current_nickname
    },
    editNickname() {
      this.editingNickname = true
      const nickname = this.nickname
      const API_URL = process.env.VUE_APP_API_URL
      // 닉네임 수정 (닉네임이 기존과 다를때 -> 회원정보 수정 요청)
      // 공백이면 에러 메세지
      if (!nickname) {
        alert("닉네임을 입력하세요!")
      }
      if (nickname != this.current_nickname) {
        axios({
          method: "PUT",
          url: `${API_URL}/api/v1/accounts/user/`,
          data: {
            nickname
          },
          headers: {
            Authorization: `Bearer ${this.$store.getters.getToken}`,
          },
        })
          .then((res) => {
            const data = {
              accessToken: this.$store.getters.getToken,
              refreshToken: this.$store.getters.getRefresh,
              user: {
                pk: res.data.pk,
                nickname: res.data.nickname
              }
            }
            this.$store.dispatch('saveUserInfo', data)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    editPassword() {
      // 비밀번호 수정
      // pw1 == pw2, 8자 이상일 때 axios 요청
      const password1 = this.password1
      const password2 = this.password2
      if (password1 && password2) {
        if (password1 < 8 || password2 < 8) {
          alert('비밀번호는 8자 이상 입력해주세요')
        } else if (password1 != password2) {
          alert('비밀번호를 다시 확인해주세요')
        } else {
          axios({
            method: 'put',
            url : `${process.env.VUE_APP_API_URL}/api/v1/accounts/password/change/`,
            headers : {
              Authorization : `Bearer ${this.$store.getters.getToken}`
            },
            data : {
              password1, password2
            }
          })
            .then((res) => {
              console.log(res)
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              this.$store.dispatch('logout')
              this.$router.push({ name: 'HomeView' })
            })
            .catch((err) => {
              console.log(err)
            })
        }
      }
    },
  },
  created() {
    this.currentNickname()
  },
}
</script>

<style>
</style>