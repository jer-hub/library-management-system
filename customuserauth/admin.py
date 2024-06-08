from django.contrib import admin
from customuserauth.models import CustomUserModel


# Register your models here.
@admin.register(CustomUserModel)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
