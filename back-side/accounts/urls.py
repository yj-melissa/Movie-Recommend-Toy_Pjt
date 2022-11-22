from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'accounts'
urlpatterns = [
    path('delete/<int:user_pk>/', views.delete_account),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
