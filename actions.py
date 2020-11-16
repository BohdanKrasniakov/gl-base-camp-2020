from abc import ABC

import pages


class SearchActions(ABC):
    SEARCH_PAGE = None

    def search_by_keyword(self, keyword):
        self.SEARCH_PAGE.search_bar.clear()
        self.SEARCH_PAGE.search_bar.send_keys(keyword)
        self.SEARCH_PAGE.search_bar.submit()


class GoogleSearchActions(SearchActions):
    def __init__(self, driver):
        self.SEARCH_PAGE = pages.GoogleSearchPage(driver)
        self.SEARCH_PAGE.open()

    def open_search_result_by_address(self, address):
        self.SEARCH_PAGE.get_search_result_by_address(address).click()


class PyPiSearchActions(SearchActions):
    def __init__(self, driver):
        self.SEARCH_PAGE = pages.PyPiSearchPage(driver)

    def open_the_second_search_result(self, keyword):
        self.search_by_keyword(keyword)
        self.SEARCH_PAGE.get_the_second_search_result().click()


class GLCareersSearchActions(SearchActions):
    def __init__(self, driver):
        self.SEARCH_PAGE = pages.GLCareersSearchPage(driver)
        self.SEARCH_PAGE.open()

    def print_first_found_job(self, job):
        self.search_by_keyword(job)
        print(f'\nYour next opportunity to become QA in GlobalLogic is {self.SEARCH_PAGE.get_the_first_search_result().text}!')
