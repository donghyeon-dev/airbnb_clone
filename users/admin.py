from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    """ Custom User Admin"""

    # list_display = ("username","email", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")


""" 5라인의 다른 형식 =  admin.site.register(models.User, CustomUserAdmin.)
admin패널의 User가 customUserADmin. class를 control"""
