<template>
  <b-container class="animate__animated animate__backInRight bv-example-row">
    <div id="con"></div>
    <b-row align-v="center" class="mt-4">
    <b-col cols="3"></b-col>
    <b-col cols="6">
    <b-card title="SIGN UP">
      <b-card-text>
        <form @submit.prevent="signUp" enctype="multipart/form-data">
          <b-row class="mt-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="email"> E-mail : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="email"
                v-model.trim="data.email"
                type="email"
                placeholder="Enter email"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="password1"> Password : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="password1"
                v-model.trim="data.password1"
                type="password"
                placeholder="Enter Password"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="password2"> Password Check : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="password2"
                v-model.trim="data.password2"
                type="password"
                placeholder="Enter Password once again"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="nickname"> Nickname : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <b-form-input
                id="nickname"
                v-model.trim="data.nickname"
                type="text"
                placeholder="Enter Your Nickname"
                required
                class="w-75"
              ></b-form-input>
            </b-col>
          </b-row>
          <b-row class="my-4" align-v="center">
            <b-col class="text-right">
              <label class="m-0" for="profile_img"> Profile Image : </label>
            </b-col>
            <b-col cols="8" class="text-center">
              <v-file-input
                accept="image/*"
                id="profile_img"
                class="w-75"
                prepend-icon="mdi-camera"
                v-model="data.profile_img"
                @change="updateImageDisplay"
              ></v-file-input>
              <div class=imgpreview></div>
              <div class="preview" v-show="imgDisplay">
                <p>No files currently selected for upload</p>
              </div>
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
      data: {
        password1: null,
        password2: null,
        email: null,
        nickname: null,
        profile_img: null,
      },      
      imgDisplay: false,
      isImg : 0,
    }
  },
  methods: {
    signUp() {
      const API_URL = process.env.VUE_APP_API_URL
      const data = this.data
      const formData = new FormData()
      formData.append('password1', data.password1)
      formData.append('password2', data.password2)
      formData.append('email', data.email)
      formData.append('nickname', data.nickname)
      if (data.profile_img === null) {
        // formData.append('profile_img', [])
      } else {
        formData.append('profile_img', data.profile_img)
      }

      const password1 = data.password1
      const password2 = data.password2
      if (password1 && password2) {
        if ((password1.length < 8) || (password2.length < 8)) {
          alert('비밀번호는 8자 이상 입력해주세요')
        } else if (password1 != password2) {
          alert('비밀번호를 다시 확인해주세요')
        } else { 
          axios({
            method: 'POST',
            url: `${API_URL}/api/v1/accounts/signup/`,
            headers: {
              'Content-Type': 'multipart/form-data',
            },
            data: formData
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
              alert(errMessage)
            })
        }
      }
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
        if(this.isImg == 1){
          alert("이미 프로필 이미지가 있습니다.")
          return
        }else{
          for(const file of curFiles) {
          const div = document.querySelector('.imgpreview');
          const para = document.createElement('p');

          if(validFileType(file)) {
            const image = document.createElement('img');
            image.src = URL.createObjectURL(file);
            // listItem.appendChild(image);
            image.setAttribute('class','w-100')
            div.appendChild(image);
            this.isImg = 1 
          } else {
            para.textContent = `${file.name}: Not a valid file type. Update your selection.`;
            div.appendChild(para);
          }
        }  
        }
        
      }
    },    

  }
}
</script>

<style scoped>
  #con{
  min-height: 100px;
}

  #img-pre{
    width: 100px;
    height: 100px;
  }
  .imgpreview{
    width: 200px;
    height: 200px;
  }
</style>>
