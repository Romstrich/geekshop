from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    image=models.ImageField(upload_to='images',blank=True)
    age=models.PositiveIntegerField(default=18)


