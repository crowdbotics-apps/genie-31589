from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GigAccountViewSet

router = DefaultRouter()
router.register("gigaccount", GigAccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
