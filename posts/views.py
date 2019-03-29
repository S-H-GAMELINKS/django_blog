from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def index(request):
    article_list = Article.objects
    return HttpResponse(article_list)
    