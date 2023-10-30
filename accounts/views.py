from accounts.models import Sponsors, Students, University
from accounts.serializers import (
    UniversitySerializer,
    SponsorsSerializer, 
    StudentsSerializer,
    DashboardSerializer
    )
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from payments.models import Sponsorship
from payments.serializers import SponsorshipSerializer
# Create your views here.

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    search_fields = ["first_name", "last_name"]
    filterset_fields = ["degree", "university"]

    @action(detail=True, methods=["get"])
    def sponsors(self, request, pk=None):
        student = self.get_object()
        queryset = student.sponsorship_set.all()
        serializer = SponsorshipSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    search_fields = ["full_name", "company"]
    filterset_fields = ["balance", "status", "sponsored"]

    @action(detail=True, methods=['get'])
    def sponsored(self, request, pk=None):
        sponsor = self.get_object()
        queryset = sponsor.sponsorship_set.all()
        serializer = SponsorshipSerializer(queryset, many=True)
        return Response(serializer.data)



class DashboardView(viewsets.ViewSet):
    def list(self, request):
        return Response({
            "payed": Sponsorship.objects.aggregate(Sum('amount'))['amount__sum'],
            "asked": Students.objects.aggregate(Sum('contract'))['contract__sum'],
            "should_payed": Students.objects.aggregate(Sum('contract'))['contract__sum'] - Sponsorship.objects.aggregate(Sum('amount'))['amount__sum'],
        })
    
    @action(detail=False, methods=['get'])
    def graph(self, request):
        return Response(DashboardSerializer().data)