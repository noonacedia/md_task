from core.models import CreateUpdateMixinModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Patient(CreateUpdateMixinModel):
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))

    class Meta:
        db_table = 'patient'


class Diagnosis(CreateUpdateMixinModel):
    name = models.CharField(verbose_name=_('Name'))
    patient = models.ForeignKey(
        to=Patient,
        on_delete=models.CASCADE,
        related_name='diagnoses',
        verbose_name=_('Patient')
    )

    class Meta:
        db_table = 'diagnosis'
