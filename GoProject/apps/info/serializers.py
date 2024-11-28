from rest_framework import serializers
from . import models


class ToursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tours
        fields = ('image', 'title', 'description', 'price', 'button_text')
        

class VisaGoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.VisaGo
        fields = ('country_icon', 'time', 'price', 'button_text')


class EasyGoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.EasyGO
        fields = ('image_icon', 'title', 'descriptions', 'button_more')


class ReviewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Reviews
        fields = ('photo', 'title', 'text', 'video', 'video_button')


class HeaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Contacts
        fields = ('phone_number', 'email', 'address')
        

class FooterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Contacts
        fields = ('phone_number', 'email', 'address', 'pictogram', 'map_link')