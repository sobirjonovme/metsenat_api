from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import SponsorStudent
from .serializers import SponsorStudentSerializer


# Create your views here.
class SponsorStudentListAPIView(ListCreateAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = SponsorStudentSerializer

    permission_classes = [permissions.IsAuthenticated]


class SponsorStudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = SponsorStudentSerializer

    permission_classes = [permissions.IsAuthenticated]
