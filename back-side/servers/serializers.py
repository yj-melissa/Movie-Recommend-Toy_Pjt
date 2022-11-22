from rest_framework import serializers
from .models import Movie,Review,SortedMovie
from community.serializers import NicknameSerializer

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = NicknameSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user', )

class MovieSerializer(serializers.ModelSerializer):
    comment_set = ReviewSerializer(many=True, read_only = True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class SortedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedMovie
        fields = '__all__'

        