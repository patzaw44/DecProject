from django.db import models


class Cars(models.Model):
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    # avg_rating = models.CharField(max_length=40)
    # rates_rating = models.IntegerField()

    def __str__(self):
        return self.car_make