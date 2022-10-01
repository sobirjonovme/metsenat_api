
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    RegisterSponsorSerializer,
    SponsorSerializer,
    UniversitySerializer,
    CreateStudentSerializer,
    StudentDetailSerializer,
)
from .models import Sponsor, University, Student

from utils.pagination import CustomPagination


# Create your views here.
# SPONSOR API VIEWS
# Register Sponsor
class RegisterSponsorAPIView(CreateAPIView):
    # for non auth users
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer


# Sponsors list
class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'total_money', 'create_at']
    pagination_class = CustomPagination


# Sponsor detail, update, delete
class SponsorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [permissions.IsAuthenticated]


# UNIVERSITY API VIEW
class UniversityListAPIView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination


# STUDENT API VIEWS
# Student create
class CreateStudentAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer

    permission_classes = [permissions.IsAuthenticated]


# Students list
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_type', 'university']
    pagination_class = CustomPagination


# Student detail, delete
class StudentDetailAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student update
class StudentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer

    permission_classes = [permissions.IsAuthenticated]
