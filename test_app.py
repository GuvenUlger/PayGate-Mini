import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# 1.Senaryo - Başarılı Ödeme İşlemi
def test_process_payment_success(client):
    payload = {"account_number": "TR1001", "amount": 1000.0}
    response = client.post('/api/v1/pay', json=payload)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['status'] == "APPROVED"
    assert data['remaining_balance'] == 4000.0

# 2.Senaryo - Yetersiz Bakiye
def test_insufficient_funds(client):
    payload = {"account_number": "TR1001", "amount": 99999.0}
    response = client.post('/api/v1/pay', json=payload)
    data = json.loads(response.data)

    assert response.status_code == 422
    assert data['status'] == "REJECTED"
    assert data['reason'] == "Insufficient funds"

# 3.Senaryo - Blokeli Hesap
def test_blocked_account(client):
    payload = {"account_number": "TR1002", "amount": 50.0}
    response = client.post('/api/v1/pay', json=payload)
    data = json.loads(response.data)

    assert response.status_code == 403
    assert data['status'] == "REJECTED"
    assert data['reason'] == "Account is not active"
                           
    

   