from rest_framework import serializers

from patients.models import Patient


class PatientsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            'id',
            'date_of_birth',
            'diagnoses',
        ]
