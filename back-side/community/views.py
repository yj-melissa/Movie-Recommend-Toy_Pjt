from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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
            serializer.save(user=request.user)
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)        

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # comments = get_list_or_404(Comment)
    # serializer = CommentSerializer(comments,many = True)
    # return Response(serializer.data)