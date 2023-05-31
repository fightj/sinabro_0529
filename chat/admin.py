from django.contrib import admin

from .models import Room, Message, one_one_Room

admin.site.register(Room),
admin.site.register(Message),
admin.site.register(one_one_Room),