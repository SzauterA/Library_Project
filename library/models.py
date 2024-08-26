from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    death_date = models.DateField(blank=True, null=True)
    death_place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title
    

    