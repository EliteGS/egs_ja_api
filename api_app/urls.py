from django.urls import path, include
from .views import Applications_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"applications", Applications_views, "applications")

urlpatterns = [
    path("api/", include(router.urls))
]