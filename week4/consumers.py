from channels.generic.websocket import AsyncWebsocketConsumer
import json
from week4.cv import FaceRecognition

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, bytes_data):
        # print(bytes_data)
        # Send message to room group
        await self.send(bytes_data=bytes_data)
