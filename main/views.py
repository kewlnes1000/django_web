from django.shortcuts import render
from main.models import Article
# Create your views here.


def index(request):
    Article.objects.all()
    return render(request, 'index/index.html', {
        'data': "Hello Django ",
        'Articles': Article,
    })
