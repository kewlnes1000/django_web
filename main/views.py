from django.shortcuts import render
from main.models import Article
from main.models import Lists
# Create your views here.


def index(request):
    return render(request, 'index/index.html', {
        'Articles': Article.objects.all(),
    })

def week1(request):
    return render(request, 'week1/index.html', {
        'Lists': Lists.objects.all(),
    })
