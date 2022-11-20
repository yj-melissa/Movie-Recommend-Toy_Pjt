from rest_framework import serializers
from .models import Article, Comment
from accounts.models import User

class NicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname',)

class ArticleListSerializer(serializers.ModelSerializer):
    user = NicknameSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'id', 'user')
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    user = NicknameSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)

class ArticleSerializer(serializers.ModelSerializer):
    user = NicknameSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
