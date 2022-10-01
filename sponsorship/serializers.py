from rest_framework import serializers

from .models import SponsorStudent
from users.serializers import SponsorSerializer, StudentSerializer


class SponsorStudentSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    sponsor_id = serializers.IntegerField(write_only=True)
    student_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SponsorStudent
        fields = ('id', 'sponsor', 'student', 'sponsor_id', 'student_id', 'amount')

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
