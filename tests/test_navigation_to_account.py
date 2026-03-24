from selenium.webdriver.support import expected_conditions as EC

from src.data import WebEndpoints, build_url
from src.locators import WebsiteLocators


class TestAccountNavigation:
    def test_navigate_to_account_page(self, driver_chrome, wait, authorized_user):
        wait.until(EC.element_to_be_clickable(WebsiteLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(build_url(WebEndpoints.PROFILE_PAGE)))

        assert wait.until(
            EC.visibility_of_element_located(WebsiteLocators.LOGOUT_BUTTON)
        ).is_displayed()
