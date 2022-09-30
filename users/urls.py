from django.urls import path

from .views import (
    SponsorListAPIView,
    RegisterSponsorAPIView,
    SponsorDetailAPIView,
)


app_name = 'users'

urlpatterns = [
    path('sponsors/', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('sponsors/register/', RegisterSponsorAPIView.as_view(), name='sponsor-register'),
    path('sponsors/<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),


]
