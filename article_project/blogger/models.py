from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank = True, null = True)
    portfolio = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateField(auto_now_add= True)
    favourite = models.ManyToManyField(Post)

    def __str__(self):
        return self.user



