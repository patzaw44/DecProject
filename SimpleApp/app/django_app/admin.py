from django.contrib import admin
from .models import CarBrand, CarModel, CarId, AddRate, AverageRate, CarsData, CarDetele, NumberOfRate, Rate, CarDetail


# Register your models here.

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(CarId)
admin.site.register(AddRate)
admin.site.register(AverageRate)
admin.site.register(CarDetele)
admin.site.register(NumberOfRate)

admin.site.register(CarsData)
admin.site.register(Rate)
admin.site.register(CarDetail)
