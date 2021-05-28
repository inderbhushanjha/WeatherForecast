from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cities(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    visited = models.CharField(max_length = 60, db_index = True)
    def __str__(self):
        return self.visited