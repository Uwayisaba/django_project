import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
   async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat_%' % self.room_name
        await self.channel_layer_group_add(
            self.room_group_name,
            self.channel_name 
           
        )
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                 'type':'tester_message',
                 'tester':'hello world',
            }
       )
   async def tester_message(self, event): 
        tester= event['tester']
       
   async def disconnect(self, close_code):
          await self.channel_layer.group_discard(
               self.room_group_name,
               self.channel_name
          )
        
   pass 