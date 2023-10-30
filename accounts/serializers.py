from rest_framework import serializers
from accounts.models import Sponsors, Students, University, TypeSponsor
from accounts.validators import phone_number, full_name
from rest_framework import validators
from django.db.models import Count


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    university_id = serializers.IntegerField(
        allow_null=False, required=True, write_only=True
        )
    
    class Meta:
        model = Students
        fields = [
            'id',
            'full_name',
            'phone_number',
            'university',
            'university_id',
            'degree',
            'contract',
            'balance',
            'created_at',
            'updated_at'
        ]

        read_only_fields = ['id', 'created_at', 'updated_at']
        

class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = [
            'id',
            'full_name',
            'phone_number',
            'balance',
            'sponsored',
            'company',
            'sponsor_type',
            'status',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        sponsor_type = validated_data['sponsor_type']
        if sponsor_type == TypeSponsor.YURIDIK:
            if validated_data['company']:
                sponsor = Sponsors.objects.create(**validated_data)
                return sponsor
            else:
                raise serializers.ValidationError('Company is required')
        
        sponsor = Sponsors.objects.create(**validated_data)
        return sponsor  
    
        
class DashboardSerializer(serializers.Serializer):
    
    def __init__(self):
        self.sponsors_count = (
            Sponsors.objects.extra({"created_at": "date(created_at)"}).values("created_at").annotate(count=Count("id")).values_list("created_at", "count")
            )
        
        self.students_count = (
            Students.objects.extra({"created_at": "date(created_at)"}).values("created_at").annotate(count=Count("id")).values_list("created_at", "count")
        )

    @property
    def data(self):
        return self.__dict__