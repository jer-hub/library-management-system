from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    call_number = models.IntegerField()
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    place_of_publication = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    copyright_date = models.DateField()
    pages = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="books", null=True)

    def __str__(self):
        return self.title


