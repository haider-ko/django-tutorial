from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerformanceIndicatorViewSet, CompetenciesViewSet, CompetencyLevelViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'performance-indicators', PerformanceIndicatorViewSet)
router.register(r'competencies', CompetenciesViewSet)
router.register(r'competency-levels', CompetencyLevelViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
