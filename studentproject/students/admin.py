from django.contrib import admin
from .models import UserRegistration
# Register your models here.
@admin.register(UserRegistration) 
class UserRegistratonAdmin(admin.ModelAdmin):
    list_display=("id","name","email","password","is_approved",)
    list_filter=("is_approved","created_at",)