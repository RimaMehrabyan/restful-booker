import pytest
import requests
import allure
import test_1_booking_token
import test_2_booking_post


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Tests')
@allure.title('Partial Update Booking Test')
@allure.description('This test verifies that a partial update to a booking is successful with valid token.')
@allure.severity(allure.severity_level.CRITICAL)
def test_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send PATCH request to partially update the booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify updated firstname is correct'):
        assert body["firstname"] == response_data["firstname"], f"Expected firstname '{body['firstname']}', but got '{response_data['firstname']}'"

    with allure.step('Verify updated lastname is correct'):
        assert body["lastname"] == response_data["lastname"], f"Expected lastname '{body['lastname']}', but got '{response_data['lastname']}'"

    with allure.step('Verify totalprice is present in the response'):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step('Verify depositpaid is present in the response'):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step('Verify bookingdates is present in the response'):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step('Verify checkin date is present in the response'):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin' in 'bookingdates'"

    with allure.step('Verify checkout date is present in the response'):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout' in 'bookingdates'"

    with allure.step('Verify additionalneeds is present in the response'):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"


    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Tests')
@allure.title('Negative Partial Update with Invalid Token Test')
@allure.description('This test verifies that a partial update to a booking with an invalid token is not permitted.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_partial_update_with_invalid_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token=12312312'}

    with allure.step('Send PATCH request to partially update the booking with an invalid token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 403, f"Expected Status Code 403, but got {response.status_code}"


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Tests')
@allure.title('Negative Partial Update Without Token Test')
@allure.description('This test verifies that a partial update to a booking without a token is not permitted.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_partial_update_without_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send PATCH request to partially update the booking without a token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 403, f"Expected Status Code 403, but got {response.status_code}"