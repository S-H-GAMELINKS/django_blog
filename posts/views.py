from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    article_list = Article.objects.all()
    template = loader.get_template('posts/index.html')
    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))
    