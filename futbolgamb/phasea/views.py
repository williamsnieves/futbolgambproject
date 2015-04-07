from django.shortcuts import render
from .models import PhaseA
from rest_framework import viewsets
from .serializers import PhaseASerializer
# Create your views here.

class PhaseAViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhaseA.objects.all()
    serializer_class = PhaseASerializer
