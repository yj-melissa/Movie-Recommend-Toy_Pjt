from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from community.serializers import ArticleListSerializer, CommentSerializer
from servers.serializers import ReviewSerializer, MovieSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=10)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname')
        return data

class UserSerializer(UserDetailsSerializer):

    article_set = ArticleListSerializer(many=True, read_only = True)
    comment_set = CommentSerializer(many = True, read_only = True)
    review_set = ReviewSerializer(many = True, read_only = True)
    likes_set = MovieSerializer(many = True, read_only = True)
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'article_set', 'comment_set', 'review_set', 'likes_set' )

    def update(self, instance, validated_data):
        # userprofile_serializer = self.fields['profile']
        # userprofile_instance = instance.userprofile
        # userprofile_data = validated_data.pop('userprofile', {})

        # to access the 'nickname' field in here
        # nickname = userprofile_data.get('nickname')

        # update the userprofile fields
        # userprofile_serializer.update(userprofile_instance, userprofile_data)

        instance = super().update(instance, validated_data)
        return instance
