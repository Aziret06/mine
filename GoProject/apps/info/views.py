from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . import models, serializers


class ToursAPIView(ListAPIView):
    serializer_class = serializers.ToursSerializer
    queryset = models.Tours.objects.all()
    

class VisaGoAPIView(ListAPIView):
    serializer_class = serializers.VisaGoSerializer
    queryset = models.VisaGo.objects.all()
    
    
class EasyGoAPIView(ListAPIView):
    serializer_class = serializers.EasyGoSerializer
    queryset = models.EasyGO.objects.all()
    
    
class ReviewsAPIView(ListAPIView):
    serializer_class = serializers.ReviewsSerializer
    queryset = models.Reviews.objects.all()    


class HeaderAPIView(ListAPIView):
    serializer_class = serializers.HeaderSerializer
    queryset = models.Contacts.objects.all()
    
    
class FooterAPIView(ListAPIView):
    serializer_class = serializers.FooterSerializer
    queryset = models.Contacts.objects.all()

