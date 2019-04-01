from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import CommentsForm

from .models import Comment, Article

def index(request):
    article_list = Article.objects.all()
    context = {
        'article_list': article_list,
    }
    return HttpResponse(render(request, 'posts/index.html', context))
    
def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist!")
    return render(request, 'posts/detail.html', {'article': article, 'form': CommentsForm})

def comments(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        Comment.objects.create(article=article, content_text=request.POST['content_text'])
        comments = Comment.objects.all()
    except Article.DoesNotExist:
        raise Http404("Article does not exist! Can not Create Comments!")

    return render(request, 'posts/detail.html', {'article': article, 'comments': comments, 'form': CommentsForm})
