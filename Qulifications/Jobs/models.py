from django.db import models

# Create your models here.

class Jobtitle(models.Model):
    namejob = models.TextField(max_length=60)
    description = models.TextField(max_length=1000)
    posttime = models.DateField(auto_now_add=True)
    #likes = models.ManyToManyField()

    def describe (self)-> str:
        return f"{self.namejob}"





class Contact(models.Model):
    pass


