from django.urls import path

from .views import (
    CreateSponsorStudentAPIView,
    SponsorStudentAPIView,
    SponsorStudentListAPIView,

    OverallStatistics,
    SponsorStatistics,
    StudentStatistics,
)

app_name = 'sponsorship'

urlpatterns = [
    path('', SponsorStudentListAPIView.as_view(), name='list'),
    path('create/', CreateSponsorStudentAPIView.as_view(), name='create'),
    path('<int:pk>/', SponsorStudentAPIView.as_view(), name='detail'),

    path('dashboard/overall-statistics/', OverallStatistics.as_view(), name='dashboard-overall'),
    path('dashboard/sponsors/', SponsorStatistics.as_view(), name='dashboard-sponsors'),
    path('dashboard/students/', StudentStatistics.as_view(), name='dashboard-students'),
]
