from django.contrib import admin

from .models import Friend, Room, Message, RoomUpdate, MessageUpdate


admin.site.register(Room)
admin.site.register(RoomUpdate) 
admin.site.register(Message)
admin.site.register(MessageUpdate)
admin.site.register(Friend)
