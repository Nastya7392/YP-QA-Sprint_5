from selenium.webdriver.support import expected_conditions as EC

from src.data import WebEndpoints, build_url
from src.locators import WebsiteLocators


class TestUserLogin:
    def test_login_via_account_button(self, driver_chrome, wait, test_user):
        driver_chrome.get(build_url(WebEndpoints.MAIN_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_INTO_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.LOGIN_PAGE)))
        wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
            test_user['email']
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
            test_user['password']
        )
        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM)).click()

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON)
        ).is_displayed()

    def test_login_via_account_button_in_header(self, driver_chrome, wait, test_user):
        driver_chrome.get(build_url(WebEndpoints.MAIN_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.LOGIN_PAGE)))
        wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
            test_user['email']
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
            test_user['password']
        )
        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM)).click()

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON)
        ).is_displayed()

    def test_login_via_registration_form(self, driver_chrome, wait, test_user):
        driver_chrome.get(build_url(WebEndpoints.REGISTER_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.LOGIN_PAGE)))
        wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
            test_user['email']
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
            test_user['password']
        )
        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM)).click()

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON)
        ).is_displayed()

    def test_login_via_forgot_password_form(self, driver_chrome, wait, test_user):
        driver_chrome.get(build_url(WebEndpoints.FORGOT_PASSWORD_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_TEXT_LINK)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.LOGIN_PAGE)))
        wait.until(EC.visibility_of_element_located(WebsiteLocators.EMAIL_INPUT_FORM)).send_keys(
            test_user['email']
        )
        wait.until(EC.visibility_of_element_located(WebsiteLocators.PASSWORD_INPUT_FORM)).send_keys(
            test_user['password']
        )
        wait.until(EC.element_to_be_clickable(WebsiteLocators.LOGIN_BUTTON_FORM)).click()

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.MAKE_ORDER_BUTTON)
        ).is_displayed()
