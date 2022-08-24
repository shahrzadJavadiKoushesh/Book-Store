from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=5)

