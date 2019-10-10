from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    """ 이 클래스는 User를 제외한 다른 어플리케이션에서 사용할예정임 """

    created = models.DateTimeField(
        auto_now_add=True
    )  # get the time when model is created
    updated = models.DateTimeField(auto_now=True)  # get the time when updated

    class Meta:
        abstract = True
        """  L11===DB로 가는 모델이 아니라 그냥 우리가 사용하는 모델이라는 뜻 """
