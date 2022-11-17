<template>
  <div id="app">
    <nav :style="{'background-color': '#302C24'}">
      <router-link :to="{name : 'HomeView'} ">Home</router-link> |
      <router-link :to="{name : 'RecommendView'} ">Recommend</router-link> |
      <router-link :to="{name : 'CommunityView'}">Community</router-link> | 
      <router-link :to="{name : 'SignUpView'}">SignUp</router-link> |
      <router-link :to="{name : 'MovieDetailView'}">Detail</router-link> |
      <router-link :to="{name : 'LoginView'}">Login</router-link>
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
    },
  },
  // methods: {
  //   getLogin

  // },
})
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #FAF9D9;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
