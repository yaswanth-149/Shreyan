from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name