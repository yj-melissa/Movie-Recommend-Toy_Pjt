from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('getarticles/', views.getarticles),
    # path('createcomment/', views.comment_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/createcomment/', views.comment_create),
    path('<int:article_pk>/comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]