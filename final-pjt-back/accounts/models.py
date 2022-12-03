from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, nickname, password, profile_img, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            nickname=nickname,
            profile_img=profile_img,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save()
        return superuser


class User(AbstractBaseUser):

    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_img = ProcessedImageField(
        upload_to='profile',
        processors=[Thumbnail(100, 100)],
        format='png',
        blank=True,
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
