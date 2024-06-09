from rest_framework import viewsets
from .models import PerformanceIndicator, Competencies
from .serializers import PerformanceIndicatorSerializer, CompetenciesSerializer


class PerformanceIndicatorViewSet(viewsets.ModelViewSet):
    queryset = PerformanceIndicator.objects.all()
    serializer_class = PerformanceIndicatorSerializer


class CompetenciesViewSet(viewsets.ModelViewSet):
    queryset = Competencies.objects.all()
    serializer_class = CompetenciesSerializer
