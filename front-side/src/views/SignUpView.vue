<template>
  <div>
    <h1>SIGN UP</h1>
    <form>
      <div class="mb-3">
        <label for="username" class="form-label m-3">username: </label>
        <input type="text" id="username">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password: null,
    }
  },
}
</script>

<style>
</style>