from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    task = models.CharField(max_length=200)
    detail = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    is_done = models.BooleanField(default=False)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task