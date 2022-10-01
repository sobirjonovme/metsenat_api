from rest_framework import serializers

from .models import Sponsor, University, Student
from sponsorship.models import SponsorStudent


# SPONSOR SERIALIZERS
class RegisterSponsorSerializer(serializers.ModelSerializer):
    # for non auth users
    class Meta:
        model = Sponsor
        fields = ('full_name', 'sponsor_type', 'phone_number', 'total_money', 'company_name')


class SponsorSerializer(serializers.ModelSerializer):
    # for admin users
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'sponsor_type', 'phone_number', 'total_money',
                  'company_name', 'create_at', 'status', 'spent_money', 'payment_type')

        read_only_fields = ['create_at', 'spent_money']


# UNIVERSITY SERIALIZER
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name')


# STUDENT SERIALIZERS
class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'phone_number', 'university', 'student_type', 'tuition_fee')


class DetailStudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorStudent
        fields = ('id', 'sponsor', 'amount')


class StudentDetailSerializer(serializers.ModelSerializer):

    university = UniversitySerializer()
    sponsorships_recieved = DetailStudentSponsorSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'phone_number', 'university', 'student_type',
                  'tuition_fee', 'create_at', 'received_money', 'sponsorships_recieved')

        read_only_fields = ('received_money', 'create_at')
