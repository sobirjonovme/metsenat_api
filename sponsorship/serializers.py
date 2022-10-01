from rest_framework import serializers

from .models import SponsorStudent
from users.serializers import SponsorSerializer, StudentDetailSerializer


class CreateSponsorStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorStudent
        fields = ('sponsor', 'student', 'amount')

    def validate(self, data):
        if data['amount'] > (data['sponsor'].total_money - data['sponsor'].spent_money):
            raise serializers.ValidationError(
                {'amount': 'Homiyda kiritilgan summa mavjud emas'}
            )
        if (data['student'].tuition_fee - data['student'].received_money) < data['amount']:
            raise serializers.ValidationError(
                {'amount': 'Talabaga keragidan ortiq summa kiritildi'}
            )
        return data


class SponsorStudentDetailSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer()
    student = StudentDetailSerializer()

    class Meta:
        model = SponsorStudent
        fields = ('id', 'sponsor', 'student', 'amount')
