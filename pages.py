from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from abc import ABC


class BasePage(ABC):
    URL = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @property
    def url(self):
        return self.URL

    def open(self):
        self.driver.implicitly_wait(10)
        self.driver.get(self.URL)

    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator),
                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}")


class SearchPage(BasePage):
    SEARCH_BAR = (By.NAME, 'q')
    SEARCH_RESULTS = None

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def search_bar(self):
        return self.find_element(self.SEARCH_BAR)

    @property
    def search_results(self):
        return self.find_elements(self.SEARCH_RESULTS)

    def search(self, keyword):
        self.search_bar.clear()
        self.search_bar.send_keys(keyword)
        self.search_bar.submit()


class GoogleSearchPage(SearchPage):
    URL = 'https://www.google.com.ua'

    def __init__(self, driver):
        super().__init__(driver)

    def get_search_result_by_address(self, address):
        return self.find_element((By.XPATH, f'//a[contains(@href,"{address}")]'))


class PyPiSearchPage(SearchPage):
    URL = 'https://www.pypi.org'

    SEARCH_RESULTS = (By.CLASS_NAME, "package-snippet")

    def __init__(self, driver):
        super().__init__(driver)

    def get_the_second_search_result(self):
        return self.search_results[1]


class GLCareersSearchPage(SearchPage):
    URL = 'https://www.globallogic.com/ua/careers/'

    SEARCH_BAR = (By.ID, 'by_keyword')
    SEARCH_RESULTS = (By.CLASS_NAME, "mb-0")

    def __init__(self, driver):
        super().__init__(driver)

    def get_the_first_search_result(self):
        return self.search_results[0]
