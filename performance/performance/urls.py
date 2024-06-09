from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from performance_indicator.views import CompetenciesViewSet, PerformanceIndicatorViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'performance-indicators', PerformanceIndicatorViewSet)
router.register(r'competencies', CompetenciesViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
