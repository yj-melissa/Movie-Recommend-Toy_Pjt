from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

from django.shortcuts import render, get_list_or_404, get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def getarticles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many = True)
        
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        
    return Response(serializer.data)

