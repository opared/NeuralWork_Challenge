from django.db import models

# Create your models here.

class ArchViajes(models.Model):
    file = models.FileField(blank=False, null=False,upload_to='data/')
    description = models.CharField(null=True,max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ArchViajes'

    def __str__(self) -> str:
        return self.file

class DatosCsv(models.Model):
    region = models.CharField(
        'region',
        max_length=50,
    )
    origin_coord = models.CharField(
        'origin_coord',
        max_length=50,
    )
    destination_coord = models.CharField(
        'destination_coord',
        max_length=50,
    )
    datetime = models.CharField(
        'datetime',
        max_length=50,
    )
    datasource = models.CharField(
        'datasource',
        max_length=50,
    )

    def __str__(self) -> str:
        return self.datetime