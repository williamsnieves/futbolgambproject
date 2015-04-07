from django.shortcuts import render
from .models import Principal
from rest_framework import viewsets
from .serializers import PrincipalSerializer
# Create your views here.

class PrincipalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer