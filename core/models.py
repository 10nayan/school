from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create a user with username, email and passsword"""
        if not email:
            raise ValueError("Email is a mandatory field")
        if not username:
            raise ValueError("Username is a mandatory field")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email, **extra_fields):
        """Create a superuser with role admin"""
        extra_fields.setdefault('role', 'admin')
        return self.create_user(email, username, password, extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['USERNAME']

    def __str__(self):
        return self.email



