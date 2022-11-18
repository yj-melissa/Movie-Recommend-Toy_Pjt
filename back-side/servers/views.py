from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import MovieListSerializer, ReviewSerializer, MovieSerializer
from .models import Movie, Review

# Create your views here.

@api_view(['GET'])
def getmovie(request):
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializer = MovieSerializer(Movies, many = True)
        return Response(serializer.data)


@api_view(['GET'])
def getreview(request):
    if request.method == 'GET':
        comments = get_list_or_404(Review)
        serializer = ReviewSerializer(comments, many = True)
        return Response(serializer.data)        

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(movie=movie)

    comments = get_list_or_404(Review)
    serializer = ReviewSerializer(comments, many = True)
    return Response(serializer.data)  
    
    # return Response(serializer.data, status=status.HTTP_201_CREATED)
    # comments = get_list_or_404(Comment)
    # serializer = CommentSerializer(comments,many = True)
    # return Response(serializer.data)