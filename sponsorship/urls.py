from django.urls import path

from .views import (
    SponsorStudentListAPIView,
    SponsorStudentDetailAPIView,
)

app_name = 'sponsorship'

urlpatterns = [
    path('list/', SponsorStudentListAPIView.as_view(), name='list'),
    path('detail/<int:pk>/', SponsorStudentDetailAPIView.as_view(), name='detail'),
]
