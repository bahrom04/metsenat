from django.shortcuts import render

from rest_framework import viewsets
from payments.serializers import SponsorshipSerializer
from payments.models import Sponsorship
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

# Create your views here.

class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']
    search_fields = [
        "sponsor__full_name",
        "sponsor__company",
        "student__first_name",
        "student__last_name",
    ]
    filterset_fields = ["amount"]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
