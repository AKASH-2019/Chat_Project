import imp
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique=True)

class RoomUpdate(models.Model):
    room_id = models.AutoField(primary_key=True)
    bitset = models.IntegerField()

class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added', )
class MessageUpdate(models.Model):
    room = models.ForeignKey(RoomUpdate, related_name="messagesupdate", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="messagesupdate", on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added', )

class Friend(models.Model):
    # user = models.ForeignKey(User, related_name="friends", on_delete=models.CASCADE)
    friend1 = models.ForeignKey(User, related_name="friend1_req", on_delete=models.CASCADE)
    friend2 = models.ForeignKey(User, related_name="friend2_req", on_delete=models.CASCADE)
    room = models.ForeignKey(RoomUpdate, related_name="friend_room", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added', )

