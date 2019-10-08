from django.contrib import admin
from . import models


@admin.register(models.Rooms)
class RoomAdmin(admin.ModelAdmin):
    pass
