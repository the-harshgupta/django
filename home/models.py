from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    
class Car(models.Model):
    name = models.CharField(max_length=200)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.name
