from django.db import models

# Create your models here.


class Cars(models.Model):
    car_make = models.CharField(max_length=30)
    model_name = models.CharField(max_length=40)

    def __str__(self):
        return self.car_make
