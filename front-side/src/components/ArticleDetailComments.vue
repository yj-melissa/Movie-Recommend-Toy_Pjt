<template>
  <div>
    <p class="m-0">{{ comment.user.nickname }}</p>
    <p class="m-0">{{ comment.content }}</p>
  </div>
</template>

<script>
export default {
    name: 'ArticleDetailComments',
    props: {
        comment: Object,
    },
}
</script>

<style>

</style>