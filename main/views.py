from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_POST,require_GET
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
    new_list = Lists(title=request.POST['text'])
    new_list.save()

    return JsonResponse({'state':True})
        
@require_GET
def list_finsh(request, list_id):
    List = Lists.objects.get(pk=list_id)
    List.completed = True
    List.save()
    return redirect('/week1')

@require_GET
def del_completed(request):
    Lists.objects.filter(completed=True).delete()
    return redirect('/week1')