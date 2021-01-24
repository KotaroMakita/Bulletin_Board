from django.db import models

# Create your models here.


class B_BoardModel(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    good = models.IntegerField()
    def __str__(self):
        return self.title


class BoardCommentModel(models.Model):
    comment = models.TextField()