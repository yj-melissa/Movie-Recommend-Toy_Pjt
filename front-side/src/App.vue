<template>
  <div id="app">
    <nav :style="{'background-color': '#000000'}">
      <b-row>
        <b-col cols="12" class="text-center">
          <router-link :to="{name : 'HomeView'} ">Home</router-link> |
          <router-link :to="{name : 'RecommendView'} ">Recommend</router-link> |
          <router-link :to="{name : 'CommunityView'}">Community</router-link>
        </b-col>
        <b-col class="text-right">
          <span v-if="isLogin">
            <router-link :to="{name : 'ProfileView' }">Profile</router-link> |
            <a id="logout" @click="logout">Logout</a>
          </span>
          <span v-else>
            <router-link :to="{name : 'LoginView'}">Login</router-link>
          </span>
        </b-col>
      </b-row>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default ({
  name: 'App',
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
  color: #CF0000;
;
}
#logout{
  color: cornsilk;
}
</style>