from django.db import models


class CarBrand(models.Model):
    car_make2 = models.CharField(max_length=40)


class CarModel(models.Model):
    model_name2 = models.CharField(max_length=40)


class CarsId(models.Model):
    car_id2 = models.CharField(max_length=40)


# class AddRate(models.Model):
#     rating2 = models.IntegerField()
#
#
# class AverageRate(models.Model):
#     avg_rating2 = models.FloatField()
#
#
# # Usuwanie po id
# class CarDeteles(models.Model):
#     id = models.ForeignKey('Car_ids', on_delete=models.CASCADE)
#
#
# class NumberOfRates(models.Model):
#     rates_rating = models.IntegerField()
#
#
# class CarsData(models.Model):
#     car_make = models.ForeignKey('Car_brand', on_delete=models.CASCADE)
#     model_name = models.ForeignKey('Car_model', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.car_make
#
#
# class Rate(models.Model):
#     """Add a rate for a car from 1 to 5 """
#     id = models.ForeignKey('Car_ids', on_delete=models.CASCADE)
#     rating = models.ForeignKey('Add_rate', on_delete=models.CASCADE)
#
#
# class CarsDetail(models.Model):
#     id = 'car_id'
#     make = models.ForeignKey('Car_brand', on_delete=models.CASCADE)
#     model = models.ForeignKey('Car_model', on_delete=models.CASCADE)
#     avg_rating = models.ForeignKey('Average_rate', on_delete=models.CASCADE)
#     rates_rating = models.ForeignKey('Number_of_rates', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.make
