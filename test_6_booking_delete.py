import pytest
import requests
import allure
import test_1_booking_token
import test_2_booking_post


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Delete Booking Tests')
@allure.title('Delete Booking by ID Test')
@allure.description('This test verifies that a booking can be successfully deleted by ID.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_booking_by_id():
    headers = {'Content-Type': 'application/json', 'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Sending DELETE request to remove the booking'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'