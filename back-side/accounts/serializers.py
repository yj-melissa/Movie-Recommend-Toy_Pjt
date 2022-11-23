from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from community.serializers import ArticleListSerializer, CommentSerializer
from servers.serializers import ReviewSerializer
from backend.settings import MEDIA_ROOT
from servers.serializers import ReviewSerializer, MovieSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30, required=False)
    profile_img = serializers.ImageField(use_url=False, required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.nickname = self.data.get('nickname', '')
        data.profile_img = self.FILES.get('profile_img', '')
        return data

class UserSerializer(UserDetailsSerializer):

    article_set = ArticleListSerializer(many=True, read_only = True)
    comment_set = CommentSerializer(many = True, read_only = True)
    review_set = ReviewSerializer(many = True, read_only = True)
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'nickname', 
            'article_set', 
            'comment_set', 
            'review_set', 
            'profile_img',
            )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
