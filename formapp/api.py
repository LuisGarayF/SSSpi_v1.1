from .models import FormSim
from rest_framework import viewsets, permissions
from .serializers import FormSimSerializer

class FormSimViewSet(viewsets.ModelViewSet):
    queryset = FormSim.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormSimSerializer







