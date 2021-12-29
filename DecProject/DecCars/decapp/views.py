from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from DecCars.decapp.forms import AutoForm
from DecCars.decapp.models import Auto
from DecCars.decapp.serializers import AutoSerializer


def test_response(request):
    return HttpResponse("Cars app")


def test_heading(request):
    auto_all = Auto.objects.all()
    # number = len(auto_all)
    return render(request, 'auto.html', {'text': auto_all})


def create_car(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'new_car.html', {'form': form})


class AutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

    def list(self, request, *args, **kwargs):
        """GET car list"""
        queryset = self.get_queryset()
        serializer = AutoSerializer(queryset, many=True)
        return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         """POST car"""
#         car = Car.objects.create(make=request.data['make'],
#                                  model=request.data['model'])
#         serializer = CarSerializer(car, many=False)
#         return Response(serializer.data)
#
#     def destroy(self, request, *args, **kwargs):
#         """DEL car/{id}"""
#         car = self.get_object()
#         self.perform_destroy(car)
#         # car.delete()
#         return Response(f"Car deleted.")
#
#
# class CarDelViewSet(viewsets.ModelViewSet):
#     """
#  test
#     """
#
#     def get_queryset(self):
#         queryset_id = Car.objects.filter(id=2)
#         return queryset_id
#     serializer_class = CarDelSerializer
#
#
# class RateViewSet(viewsets.ModelViewSet):
#     """Add rate for car (scale: 1-5)"""
#     queryset = NewRate.objects.all()
#     serializer_class = RateSerializer
#
#     def create(self, request, *args, **kwargs):
#         """POST rate"""
#         rate = NewRate.objects.create(car_id=request.data['id'], rating=request.data['rating'])
#         serializer = RateSerializer(rate, many=False)
#         return Response(serializer.data)
#
#
# class AllCarsViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarAllSerializer
#
#     def get_queryset(self):
#         queryset = Car.objects.filter(model="Golf")
#
#     def list(self, request, *args, **kwargs):
#         """GET list cars"""
#         queryset = self.get_queryset()
#         serializer = CarAllSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, *args, **kwargs):
#         """GET /cars/{id}"""
#         instance = self.get_object()
#         serializer = CarDelSerializer(instance)
#         return Response(serializer.data)
#
#     @action(detail=False, methods="post")
#     def avgrate(self, request, rating, **kwargs):
#         rating = NewRate.rating.get_object()
#         new_rate = Car.objects.all()
#         avg_rating = sum(rating) / len(rating)
#         new_rate.update(avg_rating=request.data['avg_rating'])
#         # new_rate.save()
#         # car = car.avg_rating.create(avg_rating=request.data[avg_rating])
#         serializer = CarAllSerializer(new_rate, many=True)
#         return Response(serializer.data)
#
#
# class PopularCarsViewSet(viewsets.ModelViewSet):
#     # queryset = Car.objects.all()
#     serializer_class = PopularSerializer
#
#     # def get_queryset(self):
#     #     rates_number = Car.objects.count('model')
#     #     queryset = Car.objects.all()
#         # queryset = Car.objects.filter(headline__contains ='model').count()
#         # return queryset
#         # rates_number = popular_car
#         # # return render(request, {'rates_number': popular_car})
#         # serializer = PopularSerializer(rates_number, many=False)
#         # return Response(serializer.data)

