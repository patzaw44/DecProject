from django.db import models


class CarBrand(models.Model):
    car_make = models.CharField(max_length=40)


class CarModel(models.Model):
    model_name = models.CharField(max_length=40)


class CarId(models.Model):
    car_id = models.IntegerField()


class AddRate(models.Model):
    rating = models.IntegerField()


class AverageRate(models.Model):
    avg_rating = models.FloatField()


class NumberOfRate(models.Model):
    rates_rating = models.IntegerField()


class CarsData(models.Model):
    make = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.car_make


# Usuwanie po id
class CarDetele(models.Model):
    Primary_key = True
    new_id = models.ForeignKey('CarId', on_delete=models.CASCADE)


class Rate(models.Model):
    """Add a rate for a car from 1 to 5 """
    # new_id = models.ForeignKey('CarId', on_delete=models.CASCADE)
    rating = models.ForeignKey('AddRate', on_delete=models.CASCADE)


class CarDetail(models.Model):
    # new_id2 = models.ForeignKey('CarId', on_delete=models.CASCADE)
    make = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE)
    avg_rating = models.ForeignKey('AverageRate', on_delete=models.CASCADE)
    rates_rating = models.ForeignKey('NumberOfRate', on_delete=models.CASCADE)

    def __str__(self):
        return self.make
