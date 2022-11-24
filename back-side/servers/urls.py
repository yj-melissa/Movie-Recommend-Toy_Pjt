from django.urls import path

from . import views

app_name = 'servers'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('getmovie/', views.getmovie),
    path('getreview/', views.getreview),
    path('<int:movie_pk>/createreview/',views.review_create),
    path('<int:movie_pk>/<int:question_number>/<int:select>/sortmovie/', views.sortmovie),
    path('<int:movie_pk>/anothermovie/',views.anothermovie),
    path('<int:movie_pk>/<int:value>/likes/', views.likes),
    path('<int:movie_pk>/likelist/', views.likeslist),
    path('<int:user_pk>/likemovielist/', views.likemovielist),
    path('<int:movie_pk>/getdetail/', views.getdetail),
    path('getsearch/', views.getsearch),
    path('<int:comment_pk>/deletereview/',views.deletereview),
]