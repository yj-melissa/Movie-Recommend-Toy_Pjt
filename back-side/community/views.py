from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
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

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(date=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # comments = get_list_or_404(Comment)
    # serializer = CommentSerializer(comments,many = True)
    # return Response(serializer.data)