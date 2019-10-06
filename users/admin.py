from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin"""

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")


""" 5라인의 다른 형식 =  admin.site.register(models.User, CustomUserAdmin.)
admin패널의 User가 customUserADmin. class를 control"""
