from rest_framework import serializers

from .models import Sponsor, University, Student


class RegisterSponsorSerializer():
    # for non auth users
    class Meta:
        model = Sponsor
        fields = ('full_name', 'sponsor_type', 'phone_number', 'total_money', 'company_name')


class SponsorSerializer(serializers.ModelSerializer):
    # for admin users
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'sponsor_type', 'phone_number', 'total_money',
                  'company_name', 'create_at', 'status', 'spent_money')

        read_only_fields = ['create_at', 'spent_money']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    # for reading
    university = UniversitySerializer(read_only=True)

    # for creating
    university_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'phone_number', 'university', 'university_id', 'student_type',
                  'tuition_fee', 'create_at', 'received_money')

        read_only_fields = ('received_money', 'create_at')

