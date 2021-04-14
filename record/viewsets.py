from rest_framework import viewsets

from .models import Record
from .serializer import RecordSerializer

class RecordViewSet(viewsets.ModelViewSet):
  queryset = Record.objects.all()
  serializer_class = RecordSerializer