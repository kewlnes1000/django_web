from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
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

@require_POST
def list_add(request):
    print(request.POST['text'])
    new_list = Lists(title=request.POST['text'])
    new_list.save()

    return JsonResponse({'state':True})
        
