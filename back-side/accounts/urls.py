from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('delete/<int:user_pk>/', views.delete_account),
]
