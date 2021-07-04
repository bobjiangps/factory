from django.db import models
from django.utils import timezone
from worker.models import Worker


class Office(models.Model):

    name = models.CharField(max_length=100, unique=True)
    ip = models.CharField(max_length=100)
    platform_name = models.CharField(max_length=100)
    platform_version = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "factory_office"


class OfficeWorker(models.Model):
    STATUS_TYPES = (
        ("active", "active"),
        ("busy", "busy"),
        ("inactive", "inactive")
    )

    office = models.ForeignKey(Office)
    worker = models.ForeignKey(Worker)
    register_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS_TYPES, default=STATUS_TYPES[0][0], max_length=100)

    def __str__(self):
        return f"office_{self.office}-worker_{self.worker}"

    class Meta:
        db_table = "factory_office_worker"
