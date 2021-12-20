from rest_framework import serializers
from .models import CarsData
""", CarDetele, Rate, CarDetail"""


class CarsDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarsData
        fields = (
            'id',
            'make',
            'model'
        )

#
# class SpeciesSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Species
#        fields = ('name', 'classification', 'language')