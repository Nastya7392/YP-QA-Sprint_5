from selenium.webdriver.support import expected_conditions as EC

from src.data import WebEndpoints, build_url
from src.locators import WebsiteLocators


class TestSectionsNavigation:
    def test_navigation_to_sections_sauces(self, driver_chrome, wait):
        driver_chrome.get(build_url(WebEndpoints.MAIN_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.SAUCES_SECTION_INACTIVE)).click()

        assert 'current' in wait.until(
            EC.visibility_of_element_located(WebsiteLocators.SAUCES_SECTION_ACTIVE)
        ).get_attribute('class')

    def test_navigation_to_sections_buns(self, driver_chrome, wait):
        driver_chrome.get(build_url(WebEndpoints.MAIN_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.SAUCES_SECTION_INACTIVE)).click()
        wait.until(EC.visibility_of_element_located(WebsiteLocators.SAUCES_SECTION_ACTIVE))
        wait.until(EC.element_to_be_clickable(WebsiteLocators.BUNS_SECTION_INACTIVE)).click()

        assert 'current' in wait.until(
            EC.visibility_of_element_located(WebsiteLocators.BUNS_SECTION_ACTIVE)
        ).get_attribute('class')

    def test_navigation_to_sections_stuffings(self, driver_chrome, wait):
        driver_chrome.get(build_url(WebEndpoints.MAIN_PAGE))

        wait.until(EC.element_to_be_clickable(WebsiteLocators.STUFFINGS_SECTION_INACTIVE)).click()

        assert 'current' in wait.until(
            EC.visibility_of_element_located(WebsiteLocators.STUFFINGS_SECTION_ACTIVE)
        ).get_attribute('class')
