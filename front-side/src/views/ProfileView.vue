<template>
  <div class="container row mt-3 animate__animated animate__fadeInRight" style="margin:0 auto">
    <div class="card col-12 p-0 row justify-content-center text-left" style="margin:0 auto">
      <h4 class="card-header py-3 text-center">
        {{ nickname }}님의 프로필 페이지
      </h4>
      <div class="card-body">
        <b-container class="bv-example-row">
          <b-row>
            <b-col cols="3">
              <b-row class="m-3">
                <h5> 현재 닉네임 : {{nickname}} </h5> <b-icon-gear class="my-1 mx-3" @click="editProfile"></b-icon-gear> 
              </b-row>
              <b-list-group>
                <b-list-group-item @click="changevalue1" :class="{'active':value==1}">작성한 글 목록</b-list-group-item>
                <b-list-group-item @click="changevalue2" :class="{'active':value==2}">작성한 댓글 목록</b-list-group-item>
                <b-list-group-item @click="changevalue3" :class="{'active':value==3}">작성한 리뷰 목록</b-list-group-item>
                <b-list-group-item @click="changevalue5" :class="{'active':value==5}">좋아하는 영화 목록</b-list-group-item>
              </b-list-group>
            </b-col>
            <b-col>
              <div> 
                <div v-if="this.value==0"> </div>
                <div v-else-if="this.value==1">
                  <h4 class="mt-4 ml-1">{{ profile.nickname }}님이 작성한 글</h4>
                  <b-list-group v-for="article in profile.article_set" :key="article.x">
                    <b-list-group-item>
                      <router-link :to="{ name: 'ArticleDetailView', params: { articleid : article.id } }">
                      {{ article.title }}
                    </router-link>
                    </b-list-group-item>
                  </b-list-group>
                </div>
                <div v-else-if="this.value==2">
                  <h4 class="mt-4 ml-1">{{ profile.nickname }}님이 작성한 댓글</h4>
                  <b-list-group>
                    <b-list-group-item v-for="comment in profile.comment_set" :key="comment.x">
                      <router-link :to="{ name: 'ArticleDetailView', params: { articleid : comment.article } }">
                        {{ comment.content }}
                      </router-link>
                    </b-list-group-item>
                  </b-list-group>
                </div>
                <div v-else-if="this.value==3">
                  <h4 class="mt-4 ml-1">{{ profile.nickname }}님이 작성한 리뷰</h4>
                  <b-list-group>
                    <b-list-group-item v-for="review in profile.review_set" :key="review.x" >
                      <router-link :to="{ name: 'MovieDetailView', params: { movieid : review.movie } }">
                        {{ review.content }}
                      </router-link>
                    </b-list-group-item>
                  </b-list-group>
                </div>
                <div v-else-if="this.value==4">
                  <ProfileEditItem
                    :current_nickname = nickname
                  />  
                </div>
                <div v-else-if="this.value==5">
                  
                  <h4 class="mt-4 ml-1">{{ profile.nickname }}님이 좋아한 영화</h4>
                  <b-list-group>
                    <b-list-group-item v-for="movie in this.likeList" :key="movie.x">
                      <p>{{movie.title}}</p>
                    </b-list-group-item>
                  </b-list-group>
                </div>
              </div>
            </b-col>
          </b-row>
        </b-container>
      </div>
      <div class="card-footer container p-2 text-right">
        <b-alert
          variant="danger"
          dismissible
          fade
          :show="Alert"
          @dismissed="Alert=false"
        >
          회원 탈퇴 후 복원은 불가능합니다. 탈퇴하시겠습니까? <b-button variant="danger" class="mx-4" @click="deleteaccount" size="sm">탈퇴하기</b-button>
        </b-alert>
        <b-button @click="alert" size="sm">회원탈퇴</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProfileEditItem from '@/components/ProfileEditItem'

export default {
  name: "ProfileView",
  components: {
    ProfileEditItem,
  },
  data() {
    return {
      nickname: null,
      profile: [],
      value : 0,
      Alert : false,
      likeList : [],
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    user() {
      return this.$store.getters.getUser
    },
  },
  methods: {
    getUser() {
      if (this.isLogin) {
        this.nickname = this.user.nickname
      } else {
        alert('로그인이 필요한 서비스입니다')
        this.$router.push({ name: 'LoginView' })
      }
    },
    getProfile() {
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/accounts/user/`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          this.profile = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkLike(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
      method : 'get',
      url: `${API_URL}/api/v1/server/${this.$store.state.user.pk}/likemovielist`,
      headers: {
        Authorization: `Bearer ${this.$store.getters.getToken}`
      }
      })
        .then((res) => {
          console.log(res)
          this.likeList = res.data
        })
        .catch((err)=>{
          console.log(err)
        })
    },

    changevalue1(){
      this.value = 1
    },
    changevalue2(){
      this.value = 2
    },
    changevalue3(){
      this.value = 3
    },
    changevalue5(){
      this.value = 5
    },
    alert(){
      this.Alert = true
    },
    deleteaccount(){
      const API_URL = process.env.VUE_APP_API_URL
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/accounts/delete/${this.$store.getters.getUser.pk}`,
        headers: {
          Authorization: `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then((res) => {
          console.log(res)
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    editProfile() {
      this.value = 4
    },

  },
  created(){
    this.getUser()
    this.getProfile()
    this.checkLike()
  },
  watch : {
    user() {
      this.getUser()
      this.getProfile()
    }
  }
}
</script>

<style>
.animate__animated.animate__fadeInRight {
  --animate-duration: 1.5s;
}
</style>