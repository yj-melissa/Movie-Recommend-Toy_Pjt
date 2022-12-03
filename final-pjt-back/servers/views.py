from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import ReviewSerializer, MovieSerializer
from .models import Movie, Review

# Create your views here.

@api_view(['GET'])
def getmovie(request):
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializer = MovieSerializer(Movies, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def getsearch(request):
    keyward = request.GET['search']
    newlist = []
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializer = MovieSerializer(Movies, many = True)
        for movie in serializer.data:
            if movie.get('title').find(keyward) == -1:
                pass
            else:
                newlist.append(movie)
                
        return Response(newlist)
    

@api_view(['GET'])
def getdetail(request,movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def getreview(request):
    if request.method == 'GET':
        comments = get_list_or_404(Review)
        serializer = ReviewSerializer(comments, many = True)
        return Response(serializer.data)

@api_view(['GET','DELETE'])
def deletereview(request,comment_pk):
    if request.method == 'DELETE':
        comment = get_object_or_404(Review, id=comment_pk)
        comment.delete()
        comments = get_list_or_404(Review)
        serializer = ReviewSerializer(comments, many = True)

        return Response(serializer.data)
        

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(movie=movie, user=request.user)
    comments = get_list_or_404(Review)
    serializer = ReviewSerializer(comments, many = True)
    return Response(serializer.data)  
    
    # return Response(serializer.data, status=status.HTTP_201_CREATED)
    # comments = get_list_or_404(Comment)
    # serializer = CommentSerializer(comments,many = True)
    # return Response(serializer.data)

@api_view(['GET'])
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
        elif question_number == 3:
            director = firstmovie.director['name']
            if select == 1:
                for movie in movie_data:
                    if movie.director['name'] == director:
                        sorted_movie.append(movie)

            elif select == 2:
                for movie in movie_data:
                    if movie.director['name'] != director:
                        sorted_movie.append(movie)
        elif question_number == 4:
            decade = firstmovie.release_date[0:3]
            if select == 1:
                for movie in movie_data:
                    if movie.release_date[0:3] == decade:
                        sorted_movie.append(movie)

            elif select == 2:
                for movie in movie_data:
                    if movie.release_date[0:3] != decade:
                        sorted_movie.append(movie)
        elif question_number == 5:
            language = "ko"
            if select == 1:
                for movie in movie_data:
                    if movie.original_language == language:
                        sorted_movie.append(movie)

            elif select == 2:
                for movie in movie_data:
                    if movie.original_language != language:
                        sorted_movie.append(movie)
        elif question_number == 6:
            actor = firstmovie.actors[1].get('name')
            if select == 1:
                for movie in movie_data:
                    for actor_d in movie.actors:
                        if actor_d.get('name') == actor:
                            sorted_movie.append(movie)
            elif select == 2:
                for movie in movie_data:
                    if actor not in movie.actors:
                        sorted_movie.append(movie)
        elif question_number == 7:
            actor = firstmovie.actors[0].get('chractor')
            if select == 1:
                for movie in movie_data:
                    for actor_d in movie.actors:
                        if actor_d.get('chractor') == actor:
                            sorted_movie.append(movie)
            elif select == 2:
                for movie in movie_data:
                    if actor not in movie.actors:
                        sorted_movie.append(movie)
                        

        serializer = MovieSerializer(sorted_movie, many= True)
        return Response(serializer.data)


@api_view(['GET'])
def anothermovie(request, movie_pk):
    movie_data = get_list_or_404(Movie)
    firstmovie = get_object_or_404(Movie, id=movie_pk)

    anothermovie = []
    actor = firstmovie.actors[0].get('name')
    genre = firstmovie.genre_ids[0]

    for movie in movie_data:
        flag = 0
        for actor_d in movie.actors:
            if actor_d.get('name') == actor:
                flag = 1
                break
        
        if flag == 1:
            anothermovie.append(movie)
            pass
        else:
            for genre_d in movie.genre_ids:
                if genre_d == genre:
                    flag = 1
        
            if flag == 1:
                anothermovie.append(movie)
    
    serializer = MovieSerializer(anothermovie, many= True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likes(request,movie_pk,value):
    movie = Movie.objects.get(pk = movie_pk)
    if value == 1:
        movie.like_users.remove(request.user)
    elif value == 0:
        movie.like_users.add(request.user)

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likeslist(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def likemovielist(request, user_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        newlist = []
        for movie in movies:
            serializer = MovieSerializer(movie)
            for user in serializer.data.get('like_users'):
                if user == user_pk:
                    newlist.append(serializer.data)
                    
        return Response(newlist)   
