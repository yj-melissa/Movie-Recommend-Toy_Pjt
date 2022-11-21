from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import SortedSerializer, ReviewSerializer, MovieSerializer
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
@api_view(['GET', 'POST'])
def sortmovie(request, movie_pk, question_number, select):
    
    sorted_movie = []

    if request.method == 'GET':
        movie_data = get_list_or_404(Movie)
        firstmovie = get_object_or_404(Movie, id=movie_pk)

        if question_number == 0:
            actor = firstmovie.actors[0].get('name')
            if select == 1:
                for movie in movie_data:
                    for actor_d in movie.actors:
                        if actor_d.get('name') == actor:
                            sorted_movie.append(movie)
            elif select == 2:
                for movie in movie_data:
                    if actor not in movie.actors:
                        sorted_movie.append(movie)
        elif question_number == 1:
            genre = firstmovie.genre_ids[0]
            if select == 1:
                for movie in movie_data:
                    if genre in movie.genre_ids:
                        sorted_movie.append(movie)
            elif select == 2:
                for movie in movie_data:
                    if genre not in movie.genre_ids:
                        sorted_movie.append(movie)
        elif question_number == 2:
            movie_date = firstmovie.release_date[0:5]
            if select == 1:
                for movie in movie_data:
                    if movie_date == movie.release_date[0:5]:
                        sorted_movie.append(movie)
            elif select == 2:
                for movie in movie_data:
                    if movie_date != movie.release_date[0:5]:
                        sorted_movie.append(movie)

        serializer = MovieSerializer(sorted_movie, many= True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     movie_data = request.data.movielist
    #     firstmovie = request.data.firstmovie

    # if question_number == 0:
    #     actor = firstmovie.actors[0]
    #     if select == 1:
    #         for movie in movie_data:
    #             if actor in movie.actors:
    #                 sorted_movie.append(movie)
    #     elif select == 2:
    #         for movie in movie_data:
    #             if actor not in movie.actors:
    #                 sorted_movie.append(movie)
    # elif question_number == 1:
    #     genre = firstmovie.genre_ids[0]
    #     if select == 1:
    #         for movie in movie_data:
    #             if genre in movie.genre_ids:
    #                 sorted_movie.append(movie)
    #     elif select == 2:
    #         for movie in movie_data:
    #             if genre not in movie.genre_ids:
    #                 sorted_movie.append(movie)
    # elif question_number == 2:
    #     movie_date = firstmovie.release_date[0:5]
    #     if select == 1:
    #         for movie in movie_data:
    #             if movie_date == movie.release_date[0:5]:
    #                 sorted_movie.append(movie)
    #     elif select == 2:
    #         for movie in movie_data:
    #             if movie_date != movie.release_date[0:5]:
    #                 sorted_movie.append(movie)

        