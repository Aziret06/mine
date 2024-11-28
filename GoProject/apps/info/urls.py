from django.urls import path
from . import views


urlpatterns = [
    path('tours/', views.ToursAPIView.as_view()),
    path('easy_go/', views.EasyGoAPIView.as_view()),
    path('visa_go/', views.VisaGoAPIView.as_view()),
    path('reviews/', views.ReviewsAPIView.as_view()),
    path('header/', views.HeaderAPIView.as_view()),
    path('footer/', views.FooterAPIView.as_view()),
]
