<template>
  <div class="home">
    {{movie.title}}
    무비
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'MoviesItems',
  props: {
    movie : Object
  },
}
</script>
