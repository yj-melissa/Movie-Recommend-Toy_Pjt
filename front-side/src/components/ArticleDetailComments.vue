<template>
  <div>
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
export default {
    name: 'ArticleDetailComments',
    props: {
        comment: Object,
    }

}
</script>

<style>

</style>