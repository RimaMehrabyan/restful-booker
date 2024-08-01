import pytest
import requests
import allure
import test_1_booking_token
import test_2_booking_post


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Update Booking Tests')
@allure.title('Update Booking Test')
@allure.description('This test verifies that a booking can be updated successfully with valid token and booking ID.')
@allure.severity(allure.severity_level.CRITICAL)
def test_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Sending PUT request to update the booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )
    with allure.step('Verifying the response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify firstname is updated correctly'):
        assert body["firstname"] == response_data["firstname"], f'Expected firstname to be {body["firstname"]}, but got {response_data["firstname"]}'

    with allure.step('Verify lastname is updated correctly'):
        assert body["lastname"] == response_data["lastname"], f'Expected lastname {body["lastname"]}, but got {response_data["lastname"]}'

    with allure.step('Verify totalprice is updated correctly'):
        assert body["totalprice"] == response_data["totalprice"], f'Expected totalprice {body["totalprice"]}, but got {response_data["totalprice"]}'

    with allure.step('Verify depositpaid is updated correctly'):
        assert body["depositpaid"] == response_data["depositpaid"], f'Expected depositpaid {body["depositpaid"]}, but got {response_data["depositpaid"]}'

    with allure.step('Verify checkin date is updated correctly'):
        assert body["bookingdates"]["checkin"] == response_data["bookingdates"]["checkin"], f'Expected checkin {body["bookingdates"]["checkin"]}, but got {response_data["bookingdates"]["checkin"]}'

    with allure.step('Verify checkout date is updated correctly'):
        assert body["bookingdates"]["checkout"] == response_data["bookingdates"]["checkout"], f'Expected checkout {body["bookingdates"]["checkout"]}, but got {response_data["bookingdates"]["checkout"]}'

    with allure.step('Verify additionalneeds is updated correctly'):
        assert body["additionalneeds"] == response_data["additionalneeds"], f'Expected additionalneeds {body["additionalneeds"]}, but got {response_data["additionalneeds"]}'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Update Booking Tests')
@allure.title('Negative Update Booking Test')
@allure.description('This test verifies that an attempt to update a booking with an invalid token results in a forbidden error.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token=457kjg'}

    with allure.step('Send PUT request with invalid token'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 403, f'Expected Status Code 403, but got {response.status_code}'

