from rest_framework import serializers
from .models import Movie,Review,SortedMovie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer):
    comment_set = ReviewSerializer(many=True, read_only = True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class SortedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedMovie
        fields = '__all__'