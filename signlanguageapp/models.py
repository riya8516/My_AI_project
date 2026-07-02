from django.db import models

# Create your models here.
from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
