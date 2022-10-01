from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from django.db import models

from users.models import Sponsor, Student
from .models import SponsorStudent
from .serializers import (
    SponsorStudentDetailSerializer,
    CreateSponsorStudentSerializer,
    DashboardSponsorSerializer,
    DashboardStudentSerializer,
)
from utils.pagination import CustomPagination


# Create your views here.
# SPONSOR_STUDENT VIEWS
# SponsorStudent create
class CreateSponsorStudentAPIView(CreateAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = CreateSponsorStudentSerializer

    permission_classes = [permissions.IsAuthenticated]


# SponsorStudent detail, update, delete
class SponsorStudentAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = CreateSponsorStudentSerializer

    permission_classes = [permissions.IsAuthenticated]


# SponsorStudent list
class SponsorStudentListAPIView(ListAPIView):
    queryset = SponsorStudent.objects.all().order_by('-id')
    serializer_class = SponsorStudentDetailSerializer

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['amount']
    pagination_class = CustomPagination


# DASHBOARD VIEWS
# Overall Sponsorship Statistics
class OverallStatistics(APIView):
    def get(self, request):
        sponsorship_money = Sponsor.objects.aggregate(total_sponsorship_money=models.Sum('spent_money'))
        required_money = Student.objects.aggregate(total_required_money=models.Sum('tuition_fee'))

        total_sponsorship_money = sponsorship_money['total_sponsorship_money']
        total_required_money = required_money['total_required_money']

        rest_required_money = total_required_money - total_sponsorship_money

        return Response({'total_sponsorship_money': total_sponsorship_money,
                         'total_required_money': total_required_money,
                         'rest_required_amount': rest_required_money})


# Dashboard Student Statistics
class SponsorStatistics(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = DashboardSponsorSerializer

    permission_classes = [permissions.IsAuthenticated]


# Dashboard Student Statistics
class StudentStatistics(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = DashboardStudentSerializer

    permission_classes = [permissions.IsAuthenticated]
