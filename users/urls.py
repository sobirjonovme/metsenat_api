from django.urls import path

from .views import (
    SponsorListAPIView,
    RegisterSponsorAPIView,
    SponsorDetailAPIView,

    UniversityListAPIView,

    CreateStudentAPIView,
    StudentListAPIView,
    StudentDetailAPIView,
    StudentUpdateAPIView,
)


app_name = 'users'

urlpatterns = [
    path('sponsors/', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('sponsors/register/', RegisterSponsorAPIView.as_view(), name='sponsor-register'),
    path('sponsors/<int:pk>/', SponsorDetailAPIView.as_view(), name='sponsor-detail'),

    path('universities/', UniversityListAPIView.as_view(), name='university-list'),

    path('students/create', CreateStudentAPIView.as_view(), name='student-create'),
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('students/<int:pk>/update', StudentUpdateAPIView.as_view(), name='student-update'),

]
