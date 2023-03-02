from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jobtitle(models.Model):
    namejob = models.TextField(max_length=60)
    description = models.TextField(max_length=1000)
    posttime = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.namejob}"
    def number_of_likes(self):
        return self.likes.count()
    








