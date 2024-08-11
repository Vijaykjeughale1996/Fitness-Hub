from django.db import models

# Create your models here. 

# class Blogger(models.Model):
#        name = models.CharField(max_length=100)
#        email = models.EmailField()

class Urls(models.Model):
    blog_name = models.CharField(max_length=100, unique=True)
    pages = models.CharField(max_length=50)
    urls = models.JSONField(default=dict)
    video_name = models.CharField(max_length=100)

