<template>
  <b-container class="bv-example-row">
    <b-row class="mb-2">
      <b-col class="text-center" cols='12'><h4 class="mt-4 ml-1">회원 정보 수정</h4></b-col>
    </b-row>
    <b-row>
      <b-col></b-col>
      <b-col cols="10">
        <b-row align-v="center" class="my-2 mb-2">
          <b-col cols="2" class="px-0"><label class="m-0" for="nickname">닉네임 : </label></b-col>
          <b-col cols="9">
            <form v-if="editingNickname" @submit.prevent="editNickname">
              <b-row>
                <b-col class="px-0">
                  <b-form-input type="text" id="nickname" v-model.trim="nickname"></b-form-input>
                </b-col>
                <b-col class="px-0"><b-button size="sm" type="submit" value="editNickname">수정</b-button></b-col>
              </b-row>
            </form>
            <div v-else @click="editNickname"><strong>{{ current_nickname }}</strong></div>
          </b-col>
        </b-row>
        <b-row class="my-2">
            <b-col v-if="profile_img_src">
              <form @submit.prevent="setProfileImg">
                <b-row>
                  <label for="profile_img">프로필 사진 : </label>
                </b-row>
                <b-row align-v="center">
                  <b-col cols="8">
                    <v-file-input
                      accept="image/*"
                      id="profile_img"
                      prepend-icon="mdi-camera"
                      v-model="profile_img"
                      @change="updateImageDisplay"
                    >
                    </v-file-input>
                  </b-col>
                  <b-col>
                    <b-button type="submit" value="editProfileImg" size="sm">수정</b-button>
                  </b-col>
                </b-row>
              </form>
            </b-col>
        </b-row>
        <b-row>
          <b-col class="preview text-center mb-3">
            <b-img rounded="circle" class="bg-dark" v-bind="imgSize" :src="profile_img_src"></b-img>
          </b-col>
        </b-row>
        <b-form @submit.prevent="editPassword">
          <b-row class="row my-2 align-items-center" align-v="center">
            <b-col cols="2" class="px-0">
              <label class="m-0 p-0" for="password1"> 비밀번호 : </label>
            </b-col>
            <b-col cols="7" class="">
              <b-form-input
                id="password1"
                v-model.trim="password1"
                type="password"
                placeholder="Enter Password"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="row my-2 align-items-center" align-v="center">
            <b-col cols="2">
              <label class="m-0" for="password2"> 재확인 : </label>
            </b-col>
            <b-col cols="7" class="">
              <b-form-input
                id="password2"
                v-model.trim="password2"
                type="password"
                placeholder="Enter Password once again"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
            <b-button cols="2" type="submit" size="sm">수정</b-button>
          </b-row>
        </b-form>
      </b-col>
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
      profile_img: null,
      
      spare : null, 

      imgSize: {
        width: 100, 
        height: 100,
      },
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
        if ((password1.length < 8) || (password2.length < 8)) {
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
              new_password2: password2,
            }
          })
            .then((res) => {
              this.spare = res.data
              localStorage.removeItem('access_token')
              localStorage.removeItem('refresh_token')
              this.$store.dispatch('logout')
              this.$router.push({ name: 'LoginView' })
            })
            .catch(() => {
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