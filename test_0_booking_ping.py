import pytest
import requests
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Ping Tests')
@allure.title('Health Check Test')
@allure.description('This test checks if the health endpoint is reachable and returns the expected status code.')
@allure.severity(allure.severity_level.BLOCKER)
def test_health_check():
    with allure.step('Send request to health check endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verifying the status code of the response'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'
