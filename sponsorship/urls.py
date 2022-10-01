from django.urls import path

from .views import (
    CreateSponsorStudentAPIView,
    SponsorStudentAPIView,
    SponsorStudentListAPIView,
)

app_name = 'sponsorship'

urlpatterns = [
    path('create/', CreateSponsorStudentAPIView.as_view(), name='create'),
    path('list/', SponsorStudentListAPIView.as_view(), name='list'),
    path('detail/<int:pk>/', SponsorStudentAPIView.as_view(), name='detail'),
]
