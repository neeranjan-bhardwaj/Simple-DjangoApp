from django.db import models

class Anime(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=False,null=True)
    Img=models.TextField(blank=False,null=True)

class User(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,unique=True)
    Password=models.CharField(max_length=100)

class UserAnimeList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watching = models.ManyToManyField(Anime, related_name='watching_users')
    plan_to_watch = models.ManyToManyField(Anime, related_name='plan_to_watch_users')