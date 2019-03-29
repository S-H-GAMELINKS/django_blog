from django.db import models

class Article(models.Model):
    title_text = models.CharField(max_length=30)  
    content_text = models.CharField(max_length=140)

class Comment(models.Model):
    content_text = models.CharField(max_length=50)
    