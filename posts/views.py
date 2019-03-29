from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import CommentsForm

from .models import Article

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list,
        'form': CommentsForm,
    }
    return HttpResponse(render(request, 'posts/index.html', context))
    
def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist!")
    return render(request, 'posts/detail.html', {'article': article})
