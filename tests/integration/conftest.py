import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework.test import APIClient

Users = get_user_model()


@pytest.fixture
def patient_group(db):
    group = Group.objects.create(name='patient')
    yield group
    group.delete()


@pytest.fixture
def doctor_group(db):
    group = Group.objects.create(name='doctor')
    yield group
    group.delete()


@pytest.fixture
def patient_user(db, patient_group):
    password = 'secretpasswordy'
    user = Users.objects.create_user(
        email='patient@gmail.com',
        password=password,
        username='mr.patient',
    )
    user.groups.add(patient_group)
    yield user
    user.delete()


@pytest.fixture
def doctor_user(db, doctor_group):
    password = 'secretpasswordy'
    user = Users.objects.create_user(
        email='doctor@gmail.com',
        password=password,
        username='mr.doctor',
    )
    user.groups.add(doctor_group)
    yield user
    user.delete()


@pytest.fixture
def patient_client(patient_user):
    client = APIClient()
    client.force_authenticate(user=patient_user)
    yield client


@pytest.fixture
def doctor_client(doctor_user):
    client = APIClient()
    client.force_authenticate(user=doctor_user)
    yield client


@pytest.fixture
def get_patients_url():
    return reverse('patients')
