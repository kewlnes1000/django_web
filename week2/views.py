from django.shortcuts import render

# Create your views here.
from week2.models import Messages
from week2.serializers import MessagesSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)