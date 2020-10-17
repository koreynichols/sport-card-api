from django.shortcuts import render
from .models import Card
from rest_framework import viewsets
from .serializers import CardSerializer
from rest_framework.decorators import api_view

# Create your views here.

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer