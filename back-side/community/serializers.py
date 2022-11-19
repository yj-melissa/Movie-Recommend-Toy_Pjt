from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # nickname = serializers.CharField()
    # comment_set = CommentSerializer(many=True, read_only = True)
    # def get_nickname(self, obj):
    #     return obj.user.nickname
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
