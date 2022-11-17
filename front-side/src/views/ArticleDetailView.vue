<template>
    <b-container class="bv-example-row">
        <b-row class="text-left">
            <b-col cols="12" >
                <b-card
                    :header="article.title"
                    style="height:600px;"
                    >
                    <b-card-text>
                      {{article.content}}</b-card-text>
                    <template #footer>
                        <b-form-textarea
                            id="textarea-rows"
                            placeholder="댓글을 입력해주세요"
                            rows="4"
                            v-model="content"
                        ></b-form-textarea>
                        <div class="text-right my-2">
                            <button>입력</button>
                        </div>
                    </template>
                </b-card>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    name : 'ArticleDetailView',
    data(){
        return {
            article : null,
        }
    },
    methods : {
        getArticleData(){
            this.article = this.$store.state.Articles[this.$route.params.articleid-1]
        }
    },
    created(){
        return this.getArticleData()
    }
}
</script>

<style>

</style>