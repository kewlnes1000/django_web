from django.shortcuts import render
from .models import PTTspider

# Create your views here.

def SpiderViewSet(request):
    SpiderInfos = PTTspider.objects.all()
    return render(request, 'week3/index.html', {
        'SpiderInfos': SpiderInfos,
    })