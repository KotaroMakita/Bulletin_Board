from django.db import models

# Create your models here.


class B_BoardModel(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    good = models.IntegerField()