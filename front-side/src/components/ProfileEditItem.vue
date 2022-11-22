<template>
  <div>
    <h4 class="mt-4 ml-1">회원 정보 수정</h4>
    <!-- 닉네임 수정 -->
    <div>
      <label for="nickname">닉네임 : </label>
      <form v-if="editingNickname" @submit.prevent="editNickname">
        <div>
          <input type="text" id="nickname" v-model.trim="nickname" />
        </div>
        <button type="submit" value="editNickname">수정하기</button>
      </form>
      <p v-else @click="editNickname">{{ current_nickname }}</p>
    </div>
    <!-- 프로필 수정 -->
    <form @submit.prevent="SetProfile">
      <label for="profile_img">프로필 사진 : </label>
      <input type="file" id="profile_img" name="profile_img" accept="image/*">
    </form>
    <!-- 비밀번호 수정 -->
    <form @submit.prevent="editPassword">
      <div>
        <label for="password1">비밀번호 : </label>
        <input type="password" id="password1" v-model.trim="password1" />
      </div>
      <div>
        <label for="password2">비밀번호 재확인: </label>
        <input type="password" id="password2" v-model.trim="password2" />
      </div>
      <button type="submit" value="editPassword">수정하기</button>
    </form>
  </div>
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
            method: 'post',
            url : `${process.env.VUE_APP_API_URL}/api/v1/accounts/password/change/`,
            headers : {
              Authorization : `Bearer ${this.$store.getters.getToken}`
            },
            data : {
              new_password1: password1, 
              new_password2: password2
            }
          })
            .then((res) => {
              console.log(res)
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              this.$store.dispatch('logout')
              this.$router.push({ name: 'LoginView' })
            })
            .catch((err) => {
              console.log(err)
            })
        }
      }
    },
    setProfile() {
      const API_URL = process.env.VUE_APP_API_URL

      axios({
        method: 'post', 
        url: `${API_URL}/api/v1/accounts/user/`,
        data: {
          // 프로필 이미지
        },
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`,
          
        },

      })
    }
  },
  created() {
    this.currentNickname()
  },
}
</script>

<style>
</style>