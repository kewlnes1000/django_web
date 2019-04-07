from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def FaceViewSet(request):
    return render(request, 'week4/index.html', {
        'room_name_json': mark_safe(json.dumps('users'))

    })

def room(request, room_name):
    return render(request, 'week4/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })