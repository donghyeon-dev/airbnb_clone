from django.db import models


class Rooms(models.Model):

    """ Room Model Definition """

    created = models.DateTimeField()
    updated = models.DateTimeField()
