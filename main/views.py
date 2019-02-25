from django.shortcuts import render
from main.models import Article
# Create your views here.


def index(request):
    Articles = Article.objects.all()
    return render(request, 'index/index.html', {
        'Articles': Articles,
    })
