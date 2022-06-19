from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
