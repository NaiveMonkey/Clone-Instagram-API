from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # abstract 을 이용해 base 로 사용함 (db에 생성 x)
    class Meta:
        abstract = True

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    captions = models.TextField()

class Comment(TimeStampedModel):

    message = models.TextField()
