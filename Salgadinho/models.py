from django.db import models

# Create your models here.
class Salgadinho(models.Model):
    id = models.AutoField(primary_key=True)
    flavor = models.CharField(max_length=20, blank=True, null=True)
    taste = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    factory_day = models.DateField()
    value = models.FloatField()