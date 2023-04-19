from django.db import models


# Create your models here.
class Contact(models.Model):
    full_name = models.TextField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    messages = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.full_name)


class Details(models.Model):
    full_name = models.TextField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.TextField()
    phonenumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(max_length=50)
    district = models.TextField()
    branch = models.TextField()
    accounttype = models.TextField()
