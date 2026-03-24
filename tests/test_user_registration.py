import requests
from selenium.webdriver.support import expected_conditions as EC

from src.data import ApiEndpoints, WebEndpoints, build_url
from src.helpers import (
    generate_invalid_password,
    generate_name,
    generate_user_payload,
)
from src.locators import WebsiteLocators

TIMEOUT = 15


class TestUserRegistration:
    def test_successful_registration(self, driver_chrome, wait):
        user_data = generate_user_payload()
        access_token = None

        try:
            driver_chrome.get(build_url(WebEndpoints.REGISTER_PAGE))

            wait.until(EC.visibility_of_element_located(WebsiteLocators.NAME_INPUT_FORM)).send_keys(
                user_data['name']
            )
            wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
                user_data['email']
            )
            wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
                user_data['password']
            )
            wait.until(EC.element_to_be_clickable(WebsiteLocators.REGISTRATION_BUTTON_FORM)).click()

            assert wait.until(
                EC.visibility_of_element_located(WebsiteLocators.LOGIN_BUTTON_FORM)
            ).is_displayed()

            login_response = requests.post(
                build_url(ApiEndpoints.LOGIN_USER),
                json={'email': user_data['email'], 'password': user_data['password']},
                timeout=TIMEOUT,
            )
            if login_response.ok:
                access_token = login_response.json().get('accessToken')
        finally:
            if access_token:
                requests.delete(
                    build_url(ApiEndpoints.USER),
                    headers={'Authorization': access_token},
                    timeout=TIMEOUT,
                )

    def test_registration_with_invalid_password(self, driver_chrome, wait):
        driver_chrome.get(build_url(WebEndpoints.REGISTER_PAGE))

        wait.until(EC.visibility_of_element_located(WebsiteLocators.NAME_INPUT_FORM)).send_keys(
            generate_name()
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
            generate_user_payload()['email']
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
            generate_invalid_password()
        )
        wait.until(EC.element_to_be_clickable(WebsiteLocators.REGISTRATION_BUTTON_FORM)).click()

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.PASSWORD_ERROR_MESSAGE)
        ).is_displayed()
