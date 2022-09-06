from django.db import models
from django.utils.timezone import now

# Create your models here.
class QrInfo(models.Model):
    info = models.CharField(max_length= 200)
    date = models.DateField(default=now)
    image = models.ImageField()