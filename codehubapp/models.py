from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=56)
    lastname=models.CharField(max_length=56)
    email=models.CharField(max_length=122)
    phone=models.IntegerField()
    city=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.firstname
