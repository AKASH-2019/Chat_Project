from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q

import json

from .forms import SignUpForm
from room.models import Friend, RoomUpdate, MessageUpdate
# Create your views here.

@login_required
def frontpage(request):
    friends = Friend.objects.filter(Q(friend1 = request.user) | Q(friend2 = request.user))

    unique_friend = set()
    for friend in friends:
        unique_friend.add(friend.friend1.username)
        unique_friend.add(friend.friend2.username)
    add_friends = User.objects.filter( ~Q(username__in = unique_friend) )

    return render(request, 'chat_app/frontpage.html', {"friends":friends, "add_friends": add_friends})

# def friendRequest(request):
#     print(friend1)
#     print(request.user)
#     user = User.objects.get(username=friend1)

#     if Friend.objects.filter(friend1 = user, friend2 = request.user).exists():
#         friends = Friend.objects.filter(friend1 = user, friend2 = request.user)
#         print(friends)
#     if Friend.objects.filter(friend1 = request.user, friend2 = user).exists():
#         friends = Friend.objects.filter(friend1 = request.user, friend2 = user)
#         print(friends[0].room_id)
        # url = "/room/"+str(friends[0].room_id)
        # print(url)
        


    
    # if(check1):
    #     print(check1)
    # if(check2):
    #     print(check2)
    # print(check1, check2)

    # n = RoomUpdate.objects.create(bitset = 1)
    # print(n.room_id) 
    # room = RoomUpdate.objects.get(room_id=n.room_id)
    # Friend.objects.create(friend = friend1, room = room)
    # Friend.objects.create(friend = friend2, room = room)
    
    # return r(request, 'chat_app/frontpage.html', {})

@api_view(['GET'])
def friendRequest(request, slug):
    # print(slug)
    n = RoomUpdate.objects.create(bitset = 1)
    print(n.room_id) 
    room = RoomUpdate.objects.get(room_id=n.room_id)
    data = Friend.objects.create(friend1 = request.user, friend2 = User.objects.get(username=slug), room = room)
    print(data.friend1)
    res = {'room': data.room.room_id}
    json.dumps(res)
    return Response(res)


def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("signup")
        # print(form.cleaned_data['username'])

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('fontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'chat_app/signup.html', {'form':form})

