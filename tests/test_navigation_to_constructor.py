from selenium.webdriver.support import expected_conditions as EC

from src.data import WebEndpoints, build_url
from src.locators import WebsiteLocators


class TestConstructorNavigation:
    def test_navigation_from_account_to_constructor_via_constructor_button(
        self,
        driver_chrome,
        wait,
        authorized_user,
    ):
        wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.PROFILE_PAGE)))
        wait.until(EC.element_to_be_clickable(WebsiteLocators.CONSTRUCTOR_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.MAIN_PAGE)))

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER)
        ).is_displayed()

    def test_navigation_from_account_to_constructor_via_logo(
        self,
        driver_chrome,
        wait,
        authorized_user,
    ):
        wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.PROFILE_PAGE)))
        wait.until(EC.element_to_be_clickable(WebsiteLocators.SERVICE_LOGO_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.MAIN_PAGE)))

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.CONSTRUCTOR_HEADER)
        ).is_displayed()
