from django.db import models

class Article(models.Model):
    title_text = models.CharField(max_length=30)  
    content_text = models.CharField(max_length=140)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='')
    content_text = models.CharField(max_length=50)
    