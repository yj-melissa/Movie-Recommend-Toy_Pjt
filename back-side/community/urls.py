from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('getarticles/', views.getarticles),
<<<<<<< HEAD
    # path('createcomment/', views.comment_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/createcomment/', views.comment_create),
=======
    path('<int:article_pk>/createcomment/', views.comment_create)
>>>>>>> e3adb2f24747955865d5c54ffe67c59b4a2d9d0c
]