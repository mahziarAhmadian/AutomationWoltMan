from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.utils import timezone


# Create your models here.
class Admins(models.Model):
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_name = models.CharField(max_length=200)
    admin_lastname = models.CharField(max_length=200)
    admin_phone = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=200)
    admin_sms_code = models.CharField(max_length=10)
    admin_permissions = ArrayField(models.CharField(max_length=100))
    other_information = models.JSONField()

    def as_dict(self):
        return {
            "admin_id": self.admin_id,
            "admin_name": self.admin_name,
            "admin_lastname": self.admin_lastname,
            "admin_phone": self.admin_phone,
            "admin_password": self.admin_password,
            "admin_sms_code": self.admin_sms_code,
            "admin_permissions": self.admin_permissions,
            "other_information": self.other_information
        }


class WaterMeters(models.Model):
    waterMeter_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    waterMeter_data = models.CharField(max_length=30)
    waterMeter_create_date = models.DateTimeField(default=datetime.now, blank=True)
    other_information = models.JSONField()

    def as_dict(self):
        return {
            "waterMeter_id": self.waterMeter_id,
            "waterMeter_data": self.waterMeter_data,
            "waterMeter_create_date": self.waterMeter_create_date,
            "other_information": self.other_information
        }
