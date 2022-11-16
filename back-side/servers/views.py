from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import render, get_list_or_404, get_object_or_404

from .serializers import MovieListSerializer
from .models import Movie

# Create your views here.

@api_view(['GET'])
def getmovie(request):
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializer = MovieListSerializer(Movies, many = True)
        return Response(serializer.data)
