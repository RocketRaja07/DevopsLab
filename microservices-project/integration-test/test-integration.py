import pytest
import requests
import os

class TestIntegration:
    def setup_method(self):
        self.auth_url = os.getenv('AUTH_SERVICE_URL')
        self.product_url = os.getenv('PRODUCT_SERVICE_URL')
        self.order_url = os.getenv('ORDER_SERVICE_URL')
        
    def test_end_to_end_order_flow(self):
        # 1. Login and get token
        login_response = requests.post(
            f"{self.auth_url}/api/auth/login",
            json={"username": "testuser", "password": "testpass"}
        )
        assert login_response.status_code == 200
        token = login_response.json()['token']
        
        # 2. Get product details
        headers = {'Authorization': f'Bearer {token}'}
        product_response = requests.get(
            f"{self.product_url}/api/products/1",
            headers=headers
        )
        assert product_response.status_code == 200
        
        # 3. Create order
        order_response = requests.post(
            f"{self.order_url}/api/orders",
            headers=headers,
            json={
                "productId": 1,
                "quantity": 1
            }
        )
        assert order_response.status_code == 201

# integration-tests/requirements.txt
pytest==7.3.1
requests==2.31.0
pytest-html==3.2.0
