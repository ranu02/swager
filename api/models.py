from django.db import models

# Create your models here.


class Cities(models.Model):
    """@Create class for cities"""
    city_name = models.CharField(blank=True, null=True, max_length=255)
    zipcode = models.CharField(blank=True, null=True, max_length=16)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = "cities"
