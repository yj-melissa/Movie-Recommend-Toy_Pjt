from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # path('index/', views.index, name = 'index'),
    path('/getarticles', views.getarticles),
    # path('/createarticle', views.createarticle)
]