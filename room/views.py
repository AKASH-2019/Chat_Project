from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

import json

from .models import Room, Message, RoomUpdate, MessageUpdate, Friend

# Create your views here.



@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms':rooms})


# previous method ....................
# @login_required
# def room(request, slug):
#     room = Room.objects.get(slug = slug)
#     message = Message.objects.filter(room=room)[0:25]

#     return render(request, 'room/room.html', {'room':room, 'messages':message})

@login_required
def room(request, slug):
    room = RoomUpdate.objects.get(room_id = slug)
    your_rooms = Friend.objects.filter(Q(friend1 = request.user) | Q(friend2 = request.user))
    
    chat_friend = ''
    if(your_rooms[0].friend1 != request.user):
        chat_friend = your_rooms[0].friend1.username 
    else:
        chat_friend = your_rooms[0].friend2.username
    print(chat_friend)
    message = MessageUpdate.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room':room, 'messages':message, 'your_rooms':your_rooms, 'chat_friend':chat_friend})

@login_required
def friends(request, friend):
    room = Room.objects.get(friend = friend)
    


