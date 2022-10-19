import json
from .models import DirectChatMessage
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class DirectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json['sender']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'sender': sender}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event['sender']
        # Create model instance of the message
        print(f'esse foi o user do scope {self.scope["user"]}')
        print(f'esse foi o sender {sender}')
        if sender == self.scope["user"].username:
            msg = DirectChatMessage(
                chat_id=self.room_name, 
                sender= await sync_to_async(User.objects.filter(username=sender).first)(),
                message=message
            )
            await sync_to_async(msg.save)()
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'sender': sender}))