# chat/routing.py
from django.urls import include, path

from . import consumers

websocket_urlpatterns = [
    path('<room_name>/', consumers.ChatConsumer),
]