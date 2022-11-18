<template>
  <div class="home">
    <h1>LOGIN</h1>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="username" class="form-label">USERNAME</label><br>
        <input type="text" id="username" v-model.trim="username">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">PASSWORD</label><br>
        <input type="password" id="password" v-model.trim="password">
      </div>
      <button type="submit" class="btn btn-primary btn-sm m-2">LOGIN</button>
      <router-link :to="{ name: 'SignUpView' }" class="btn btn-outline-primary btn-sm m-2">SIGNUP</router-link>
    </form>
  </div>
</template>

<script>

// @ is an alias to /src
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      
      const payload = {
        username, password,
      }

      this.$store.dispatch('login', payload)
    },
  },
}
</script>
