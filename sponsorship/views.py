from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import SponsorStudent
from .serializers import SponsorStudentDetailSerializer, CreateSponsorStudentSerializer


# Create your views here.
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


class SponsorStudentListAPIView(ListAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = SponsorStudentDetailSerializer

    permission_classes = [permissions.IsAuthenticated]
