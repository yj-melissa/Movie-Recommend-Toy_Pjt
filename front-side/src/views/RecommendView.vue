<template>
  <div class="TextAnime1">
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
          <p
            v-for="(t, index) in text"
            :key="index"
            class="item"
            :style="{animationDelay: index*100+'ms'}"
            v-text="t"
          />
        </b-col>
        <b-col><img src="https://cdn0.iconfinder.com/data/icons/streamline-emoji-1/48/178-man-astronaut-2-512.png" alt=""></b-col>
      </b-row>
      <b-row>
        <b-col>
          <p
            v-for="(t, index) in text2"
            :key="index"
            class="item"
            :style="{animationDelay: index*100+'ms'}"
            v-text="t"
          />
        </b-col>
        <b-col>

        </b-col>
      </b-row>
    </b-container>
    
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: '좋아하는 영화를 하나 생각하세요',
      text2: '생각하셨나요?'
    }
  },
  name: 'RecommendView',
  components: {
  }
}
</script>

<style scoped>
@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 2rem;
  animation: text-in .8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
  color: #FAF9D9;
}
</style>
