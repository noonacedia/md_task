import pytest
from pytest_lazy_fixtures import lf
from rest_framework import status


@pytest.mark.parametrize(
    'given_client, expected_status_code',
    (
        (lf('client'), status.HTTP_401_UNAUTHORIZED),
        (lf('patient_client'), status.HTTP_403_FORBIDDEN),
        (lf('doctor_client'), status.HTTP_200_OK),
    ),
)
@pytest.mark.django_db
def test_pytest(given_client, expected_status_code, get_patients_url):
    response = given_client.get(get_patients_url)
    assert response.status_code == expected_status_code
