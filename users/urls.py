from django.urls import path

from .views import SponsorListCreateAPIView


app_name = 'users'

urlpatterns = [
    path('sponsors/', SponsorListCreateAPIView.as_view(), name='sponsor-list'),

]
