from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StageoneSerializer
from .models import Stageone

# Create your views here.


class StageoneViewset(viewsets.ModelViewSet):
    queryset = Stageone.objects.all().order_by('slack_name')
    serializer_class = StageoneSerializer
