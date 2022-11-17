from django.urls import path

from . import views

app_name = 'servers'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('server/getmovie/', views.getmovie)
]