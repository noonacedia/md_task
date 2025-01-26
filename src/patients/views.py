from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from src.patients.models import Patient
from src.patients.permissions import IsDoctor
from src.patients.serializers import PatientsListSerializer


class GetPatients(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientsListSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
