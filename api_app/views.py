from rest_framework import viewsets
from .serializer import applications_serializers
from .models import Applications

class Applications_views(viewsets.ModelViewSet):
    serializer_class = applications_serializers
    queryset = Applications.objects.all()