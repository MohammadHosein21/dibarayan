from django.db import models


# Create your models here.

class DataModel(models.Model):
    stream_id = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1)
    log = models.JSONField()
    session_id = models.CharField(max_length=36)

    class Meta:
        db_table = "data"
