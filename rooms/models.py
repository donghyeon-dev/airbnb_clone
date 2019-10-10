from django.db import models  # django's models
from django_countries.fields import CountryField  # THIRD_PARTY_APPS
from core import models as core_models  # MY MODEL
from users import models as user_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)  # required!!
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)  # required
    price = models.IntegerField()  # required
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 0 ~ 24 hour
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

