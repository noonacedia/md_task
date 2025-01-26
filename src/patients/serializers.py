from rest_framework import serializers

from patients.models import Diagnosis, Patient


class DiagnosisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnosis
        fields = ['id', 'name']


class PatientsListSerializer(serializers.ModelSerializer):
    diagnoses = DiagnosisSerializer(many=True)

    class Meta:
        model = Patient
        fields = [
            'id',
            'date_of_birth',
            'diagnoses',
        ]
