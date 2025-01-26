from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from patients.models import Patient
from patients.permissions import IsDoctor
from patients.serializers import PatientsListSerializer


class GetPatients(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientsListSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
