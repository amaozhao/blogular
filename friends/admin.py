# coding: utf-8
from django.contrib import admin

from friends.models import FriendShip


@admin.register(FriendShip)
class FriendShipAdmin(admin.ModelAdmin):
    pass
