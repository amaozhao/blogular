# coding: utf-8
from django.contrib import admin

from friends.models import FriendShip, FollowingTag


@admin.register(FriendShip)
class FriendShipAdmin(admin.ModelAdmin):
    pass


@admin.register(FollowingTag)
class FollowingTagAdmin(admin.ModelAdmin):
    pass
