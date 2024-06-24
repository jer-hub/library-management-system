from django.contrib import admin
from .models import Department, Book

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author"]