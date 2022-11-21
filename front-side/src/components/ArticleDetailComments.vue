<template>
  <div>
    <p class="m-0">{{ comment.user.nickname }}</p>
    <span v-if="!isEdit">
        <p class="m-0" >{{ comment.content }}</p>
    </span>
    <div v-show="isAuthor">
      <span v-if="isEdit">
        <textarea rows="1" v-model.trim="content"></textarea>
        <button @click="saveEdit">등록</button>
      </span>
      <button @click="editComment" id="editBtn">수정</button>
      <button @click="deleteComment">X</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "ArticleDetailComments",
  props: {
    comment: Object,
  },
  data() {
    return {
      isEdit: false,
      content: null,
      isAuthor: false,
    }
  },
  methods: {
    editComment() {
      this.content = this.comment.content
      this.isEdit = !this.isEdit
    },
    saveEdit(){
      const content = this.content
      if (!content) {
        alert("댓글을 입력해주세요")
        return
      } else {
        axios({
          method : 'put',
          url : `${process.env.VUE_APP_API_URL}/api/v1/community/comments/${this.comment.id}/`,
          headers : {
            Authorization : `Bearer ${this.$store.getters.getToken}`
          },
          data : {
            content : content
          }
        })
          .then((res)=> {
            const data = res.data
            console.log(data)
            this.isEdit = false
            this.$emit('comment-update')
          })
          .catch((err)=> {
            console.log(err)
          })
      }
    },
    deleteComment() {
      axios({
        method: 'delete',
        url: `${process.env.VUE_APP_API_URL}/api/v1/community/comments/${this.comment.id}/`,
        headers : {
          Authorization : `Bearer ${this.$store.getters.getToken}`
        }
      })
        .then(() => {
          this.$emit('comment-update')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkAuthor() {
      const user = this.$store.getters.getUser.pk
      const author = this.comment.user.id
      if (user == author) {
        this.isAuthor = true
      }
      console.log(this.isAuthor)
    },
  },
  created() {
    this.checkAuthor()
  }
}
</script>

<style>
</style>