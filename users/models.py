from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICE = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICE = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICE, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)
    """ DB상에서 black와 null은 차이가 있음 => null=True일 경우에는 유저등록시 required로 나오기 때문에 blank사용 """
    """ model에서 새로운 모델을 작업한 후 makemigration > migrate  """
