from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()


class DataModel(models.Model):
    stream_id = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1, choices=[('D', 'Danger'), ('S', 'Safe')])
    log = models.JSONField()
    session_id = models.UUIDField()

    def __str__(self):
        return f"ClientData {self.id}"

    class Meta:
        db_table = "Data"
