from django.urls import path

from . import views

app_name = 'servers'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('getmovie/', views.getmovie),
    path('getreview/', views.getreview),
    path('<int:movie_pk>/createreview/',views.review_create),
]