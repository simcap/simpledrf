from django.db import models

class City(models.Model):
    name = models.CharField(max_length=20)
    lat = models.FloatField()
    lon = models.FloatField()
    temperature = models.FloatField(null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
