import pytest
import requests
import allure
import test_2_booking_post


@allure.feature('Booking Feature')
@allure.suite('Get Booking Tests')
@allure.title('Get All Bookings')
@allure.description('This test checks the retrieval of all bookings from the Booking Service.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Sending GET request to /booking endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verifying the status code of the response'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the response contains a list of bookings'):
        assert len(response.json()) > 0, 'The List should not be Empty'


@allure.feature('Booking Feature')
@allure.suite('Get Booking Tests')
@allure.title('Get Booking by ID')
@allure.description('This test checks the retrieval of a specific booking by ID from the Booking Service.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_id():
    with allure.step('Send request to get booking by ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}')
    with allure.step('Verifying the status code of the response'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "firstname"'):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step('Verify response contains "lastname"'):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"

    with allure.step('Verify response contains "totalprice"'):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step('Verify response contains "depositpaid"'):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step('Verify response contains "bookingdates"'):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step('Verify "bookingdates" contains "checkin"'):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step('Verify "bookingdates" contains "checkout"'):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step('Verify response contains "additionalneeds"'):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step('Verify "depositpaid" is a boolean'):
        assert isinstance(response_data['depositpaid'], bool), 'ERROR: depositpaid should be a boolean'

    with allure.step('Verify "totalprice" is a number'):
        assert isinstance(response_data['totalprice'],(int, float)), 'ERROR: totalprice should be an integer or float'



