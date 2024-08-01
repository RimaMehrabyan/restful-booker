import pytest
import requests
import allure
my_bookingid = 0

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Booking Tests')
@allure.title('Create Booking Test')
@allure.description('This test verifies that a booking is successfully created with valid details.')
@allure.severity(allure.severity_level.BLOCKER)
def test_create_booking():
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a new booking'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )

    with allure.step('Verifying the response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains bookingid'):
        assert "bookingid" in response_data, "The response does not contain 'bookingid'"

    with allure.step('Verify response contains booking data'):
        assert "booking" in response_data, "The response does not contain 'booking'"

    response_booking = response_data['booking']

    with allure.step('Verify response contains "firstname"'):
        assert 'firstname' in response_booking, "The response doesn't contain 'firstname'"

    with allure.step('Verify response contains "lastname"'):
        assert 'lastname' in response_booking, "The response doesn't contain 'lastname'"

    with allure.step('Verify response contains "totalprice"'):
        assert 'totalprice' in response_booking, "The response doesn't contain 'totalprice'"

    with allure.step('Verify response contains "depositpaid"'):
        assert 'depositpaid' in response_booking, "The response doesn't contain 'depositpaid'"

    with allure.step('Verify response contains "bookingdates"'):
        assert 'bookingdates' in response_booking, '"bookingdates" not found in response'

    with allure.step('Verify "bookingdates" contains "checkin"'):
        assert 'checkin' in response_booking['bookingdates'], '"checkin" not found in "bookingdates"'

    with allure.step('Verify "bookingdates" contains "checkout"'):
        assert 'checkout' in response_booking['bookingdates'], '"checkout" not found in "bookingdates"'

    with allure.step('Verify response contains "additionalneeds"'):
        assert 'additionalneeds' in response_booking, '"additionalneeds" not found in response'

    with allure.step('Verify "firstname" is correct'):
        assert response_booking['firstname'] == data['firstname'], f"Expected firstname to be {data['firstname']}, but got '{response_booking['firstname']}'"

    with allure.step('Verify "lastname" is correct'):
        assert response_booking['lastname'] == data['lastname'], f"Expected lastname to be {data['lastname']}, but got '{response_booking['lastname']}'"

    with allure.step('Verify "totalprice" is correct'):
        assert response_booking['totalprice'] == data['totalprice'], f"Expected totalprice to be {data['totalprice']}, but got '{response_booking['totalprice']}'"

    with allure.step('Verify "depositpaid" is correct'):
        assert response_booking['depositpaid'] == data['depositpaid'], f"Expected depositpaid to be {data['depositpaid']}, but got '{response_booking['depositpaid']}'"

    with allure.step('Verify "checkin" date is correct'):
        assert response_booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f"Expected checkin to be {data['bookingdates']['checkin']}, but got {response_booking['bookingdates']['checkin']}"

    with allure.step('Verify "checkout" date is correct'):
         assert response_booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout to be {data['bookingdates']['checkout']}, but got {response_booking['bookingdates']['checkout']}"

    with allure.step('Verify "additionalneeds" is correct'):
        assert response_booking['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds to be {data['additionalneeds']}, but got '{response_booking['additionalneeds']}'"

    global my_bookingid
    my_bookingid = response_data['bookingid']