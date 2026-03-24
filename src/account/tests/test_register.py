import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_register_success(client, db):
    url = reverse("account-user-register")
    data = {
        "email": "testuser@example.com",
        "password": "strongpassword123",
    }

    response = client.post(url, data)

    assert response.status_code == 302

    user = User.objects.get(email="testuser@example.com")
    assert user.check_password("strongpassword123")
