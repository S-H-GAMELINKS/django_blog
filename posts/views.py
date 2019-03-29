from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list,
    }
    return HttpResponse(render(request, 'posts/index.html', context))
    