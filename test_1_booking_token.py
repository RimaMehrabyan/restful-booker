import pytest
import requests
import allure

my_token = None


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Authentication Feature')
@allure.suite('Token Tests')
@allure.title('Create Authentication Token')
@allure.description('This test verifies that an authentication token is successfully created with valid credentials.')
@allure.severity(allure.severity_level.BLOCKER)
def test_booking_create_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to /auth endpoint to create token'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/auth',
            headers=headers,
            json=body
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 200, f"Expected Status Code 200, but got {response.status_code}"

    with allure.step('Checking if the token is present in the response'):
         assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Checking if the token is not empty'):
        assert len(response.json().get('token')) > 0, 'Token should not be empty or None'


    global my_token
    my_token = response.json().get('token')
