from django.db import models

# Create your models here.

class CyberBreachData(models.Model):
    entity = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    records = models.CharField(max_length=255)
    org_type = models.CharField(max_length=255)
    methods = models.CharField(max_length=255)
    add_data_val = models.CharField(max_length=255, blank=True, null=True)
    time_val = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entity} - {self.year}"