<template>
  <div id="app">
    <nav class="py-1" :style="{'background-color': '#000000'}">
      <b-row align-v="center">
        <b-col>
          <router-link :to="{name : 'HomeView'} "><img src="http://127.0.0.1:8000/media/logo.png" alt="logo" width="150" height="80"></router-link>
        </b-col>
        <b-col>
            <router-link :to="{name : 'HomeView'} ">Home</router-link> |
            <router-link :to="{name : 'RecommendView'} ">Recommend</router-link> |
            <router-link :to="{name : 'CommunityView'}">Community</router-link>
        </b-col>
        <b-col>
          <span v-b-modal.modal-prevent-closing class="text-warning mr-3"> Search <b-icon icon="search" variant="warning" font-scale="1"></b-icon></span> 
          <span v-if="isLogin">
            <router-link :to="{name : 'ProfileView' }"> Profile</router-link> |
            <a id="logout" @click="logout">Logout</a>
          </span>
          <span v-else>
            <router-link :to="{name : 'LoginView'}">Login</router-link>
          </span>
        </b-col>
      </b-row>

      <b-modal id="modal-prevent-closing" title="영화 검색하기"
      ref="modal"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk">
        <form ref="form" @submit.stop.prevent="handleSubmit">
          <b-form-group
            label="제목을 입력해주세요"
            label-for="search-input"
            invalid-feedback="검색어를 입력해주세요"
            :state="searchState"
          >
            <b-form-input
              id="search-input"
              v-model="search"
              :state="searchState"
              required
            ></b-form-input>
          </b-form-group>
        </form>
      </b-modal>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default ({
  name: 'App',
  data(){
    return{
      search: '',
      searchState: null,
      logoImg : null
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {      
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.$store.dispatch('logout')
      this.$router.push({ name: 'LoginView' }) 
    },
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity()
      this.searchState = valid
      return valid
    },
    resetModal() {
      this.search = ''
      this.searchState = null
    },
    handleOk(bvModalEvent) {
      // Prevent modal from closing
      bvModalEvent.preventDefault()
      // Trigger submit handler
      this.handleSubmit()
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return
      }
      // Push the name to submitted names
      console.log(this.search)
      this.$router.push({ name: 'SearchView',params: { serchname : this.search } }) 
      // Hide the modal manually
      this.$nextTick(() => {
        this.$bvModal.hide('modal-prevent-closing')
      })
    }

  },
})
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
  background-image: url('https://th.bing.com/th/id/R.206d1860d16a9508f78744907f334f07?rik=BZbNqlbckMZm5A&riu=http%3a%2f%2fblogfiles.naver.net%2f20150205_285%2fminsoozoa_1423097179566qIcyl_JPEG%2f51.jpg&ehk=%2fTX9t9GBIhdLmN1eug268CvxKAdnzxgolzPw9XEaSMA%3d&risl=&pid=ImgRaw&r=0');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  min-height: 1000px;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size : cover;
}
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #FAF9D9;
}
nav a.router-link-exact-active {
  color: #ffc107;
;
}
#logout{
  color: cornsilk;
}
</style>