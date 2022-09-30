from rest_framework import serializers

from .models import Sponsor, Student


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'sponsor_type', 'phone_number', 'total_money',
                  'company_name', 'create_at', 'status', 'spent_money')

        read_only_fields = ['create_at', 'spent_money']
