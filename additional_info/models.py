from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=20, decimal_places=18)
    longitude = models.DecimalField(max_digits=20, decimal_places=18)

    class Meta:
        app_label = 'additional_info'
