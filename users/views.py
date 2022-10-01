
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
from rest_framework import permissions

from .serializers import (
    RegisterSponsorSerializer,
    SponsorSerializer,
    UniversitySerializer,
    CreateStudentSerializer,
    StudentDetailSerializer,
)
from .models import Sponsor, University, Student


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


# Student detail, update, delete
class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    permission_classes = [permissions.IsAuthenticated]
