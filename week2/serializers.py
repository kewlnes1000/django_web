from rest_framework import serializers
from week2.models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        # fields = ('id', 'url', 'subject', 'text', 'to', 'sent')