from django.db import models

class Anime(models.Model):
    Name=models.CharField(max_length=100)
    description=models.TextField(blank=False,null=True)
    Img=models.TextField(blank=False,null=True)