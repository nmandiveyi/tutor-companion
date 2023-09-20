from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField(max_length=50, unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  password = models.CharField(max_length=1000)
  username = None
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
