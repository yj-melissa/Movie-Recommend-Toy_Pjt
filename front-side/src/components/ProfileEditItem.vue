<template>
  <div>
    <h4 class="mt-4 ml-1">회원 정보 수정</h4>
    <!-- 닉네임 수정 -->
    <div>
      <label for="nickname" @click="editNickname">닉네임 : </label>
      <form v-if="editingNickname" @submit.prevent="editNickname">
        <div>
          <input type="text" id="nickname" v-model.trim="nickname"/>
        </div>
        <button type="submit" value="editNickname">수정하기</button>
      </form>
      <p v-else @click="editNickname">{{ current_nickname }}</p>
    </div>
    <!-- 프로필 수정 -->
    <form @submit.prevent="setProfileImg">
      <label for="profile_img">프로필 사진 : </label>
      <v-file-input
        accept="image/*"
        id="profile_img"
        class="w-75"
        prepend-icon="mdi-camera"
        v-model="profile_img"
        @change="updateImageDisplay"
      ></v-file-input>
      <div class="preview">
        <img :src="profile_img_src">
      </div>
      <button type="submit" value="editProfileImg">수정하기</button>
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
      profile_img: null,
    }
  },
  props: {
    current_nickname: String,
    profile_img_src: String,
  },
  methods: {
    currentNickname() {
      this.nickname = this.current_nickname
    },
    editNickname() {
      this.editingNickname = true
      const nickname = this.nickname
      const API_URL = process.env.VUE_APP_API_URL
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
    setProfileImg() {
      const API_URL = process.env.VUE_APP_API_URL
      const formData = new FormData()
      formData.append('nickname', this.nickname)
      if (this.profile_img === null) {
        formData.append('profile_img', [])
      } else {
        formData.append('profile_img', this.profile_img)
      }

      axios({
        method: 'PUT',
        url: `${API_URL}/api/v1/accounts/user/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`,
          'Content-Type': 'multipart/form-data',
        },
        data: formData
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
        .catch((err) => {
          const errMessage = err.response.request.response
          console.log(errMessage)
          alert(errMessage)
        })
    },
    updateImageDisplay() {
      this.imgDisplay = true
      console.log(this.profile_img)
      const input = document.querySelector('#profile_img')
      const preview = document.querySelector('.preview')

      function validFileType(file) {
        const fileTypes = [
            'image/apng',
            'image/bmp',
            'image/gif',
            'image/jpeg',
            'image/pjpeg',
            'image/png',
            'image/svg+xml',
            'image/tiff',
            'image/webp',
            `image/x-icon`
        ]
        return fileTypes.includes(file.type);
      }

      while(preview.firstChild) {
        preview.removeChild(preview.firstChild);
      }
      const curFiles = input.files;
      if(curFiles.length != 0) {
        const list = document.createElement('ol');
        preview.appendChild(list);

        for(const file of curFiles) {
          const listItem = document.createElement('span');
          const para = document.createElement('p');

          if(validFileType(file)) {
            const image = document.createElement('img');
            image.src = URL.createObjectURL(file);

            listItem.appendChild(image);
          } else {
            para.textContent = `${file.name}: Not a valid file type. Update your selection.`;
            listItem.appendChild(para);
          }
          list.appendChild(listItem);
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