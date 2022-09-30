from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

from .serializers import SponsorSerializer
from .models import Sponsor


# Create your views here.
class SponsorListCreateAPIView(ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [permissions.IsAuthenticated]

