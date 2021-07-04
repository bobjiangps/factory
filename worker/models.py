from django.db import models
from django.utils import timezone


class Worker(models.Model):

    name = models.CharField(max_length=100, unique=True)
    ip = models.CharField(max_length=100)
    platform_name = models.CharField(max_length=100)
    platform_version = models.CharField(max_length=100)
    support_browser = models.CharField(max_length=500)
    support_mobile = models.CharField(max_length=500)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "factory_worker"
