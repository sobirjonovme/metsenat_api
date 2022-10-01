from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import permissions

from .serializers import RegisterSponsorSerializer, SponsorSerializer, UniversitySerializer, StudentSerializer
from .models import Sponsor, University, Student


# Create your views here.
class RegisterSponsorAPIView(CreateAPIView):
    # for non auth users
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [permissions.IsAuthenticated]


class SponsorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [permissions.IsAuthenticated]


class UniversityListAPIView(ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [permissions.IsAuthenticated]
