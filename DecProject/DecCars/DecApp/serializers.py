from .models import Car, NewRate
from rest_framework import serializers


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']


class CarDelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'model']

class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewRate
        fields = ['id', 'rating' ]

class CarAllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

class PopularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
