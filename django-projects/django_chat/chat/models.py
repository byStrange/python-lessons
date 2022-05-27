# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import User
# # message app


# class MessageUser(models.Model):
#     """
#     MessageUser model
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     name = models.CharField(max_length=100)

#     username = models.CharField(max_length=100, unique=True)

#     avatar = models.ImageField(upload_to='avatars/')

#     def __str__(self):
#         return self.user.username


# class Room(models.Model):
#     """
#     A room for people to chat in.
#     """

#     # Room title
#     title = models.CharField(max_length=255)

#     # If only "staff" users are allowed (is_staff on django's User)
#     # staff_only = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


# class Message(models.Model):
#     """
#     The chat messages
#     """

#     # Author of the message
#     user = models.ForeignKey(MessageUser, on_delete=models.CASCADE)

#     # The message
#     message = models.TextField()

#     # The room it was posted to
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)

#     # The time it was posted at
#     timestamp = models.DateTimeField(auto_now_add=True)

from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)