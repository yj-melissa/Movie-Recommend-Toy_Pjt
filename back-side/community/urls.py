from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('getarticles/', views.getarticles),
    path('<int:article_pk>/createcomment/', views.comment_create)
]