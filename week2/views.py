import requests
from django.shortcuts import render
from rest_framework import status, viewsets
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from week2.models import Messages
from week2.serializers import MessagesSerializer


# Create your views here.
class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    # parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.action not in ('list',):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    # [POST] api/Messages/
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        subject = request.data.get('subject')
        text = request.data.get('text')
        to = request.data.get('to')
        response = requests.post(
            "https://api.mailgun.net/v3/sandbox4427d941550c4d92ab6b1b1f553ec3dd.mailgun.org/messages",
            auth=("api", "0b5387dc6df516285816ee148d6acf3c-7caa9475-978cf5da"),
            data={"from": "Excited User <mailgun@sandbox4427d941550c4d92ab6b1b1f553ec3dd.mailgun.org>",
                "to": [to],
                "subject": subject,
                "text": text})
        print(response)
        if response.ok:
            message = Messages.objects.create(subject=subject, text=text, to=to, sent=True)
        else:
            message = Messages.objects.create(subject=subject, text=text, to=to)
            
        serializer = MessagesSerializer(message)



        return Response(serializer.data, status=status.HTTP_201_CREATED)
