from abc import ABC

import pages


class SearchActions(ABC):
    SEARCH_PAGE = None

    def search_by_keyword(self, keyword):
        self.SEARCH_PAGE.search_bar.clear()
        self.SEARCH_PAGE.search_bar.send_keys(keyword)
        self.SEARCH_PAGE.search_bar.submit()


class GoogleSearchActions(SearchActions):
    def __init__(self, browser):
        self.SEARCH_PAGE = pages.GoogleSearchPage(browser)
        self.SEARCH_PAGE.open()

    def open_search_result_by_address(self, address):
        result = self.SEARCH_PAGE.get_search_result_by_address(address)
        self.SEARCH_PAGE.click(result)


class PyPiSearchActions(SearchActions):
    def __init__(self, browser):
        self.SEARCH_PAGE = pages.PyPiSearchPage(browser)

    def open_the_second_search_result(self, keyword):
        self.search_by_keyword(keyword)
        result = self.SEARCH_PAGE.get_the_second_search_result()
        self.SEARCH_PAGE.click(result)


class GLCareersSearchActions(SearchActions):
    def __init__(self, browser):
        self.SEARCH_PAGE = pages.GLCareersSearchPage(browser)
        self.SEARCH_PAGE.open()

    def print_first_found_job(self, job):
        self.search_by_keyword(job)
        print(f'\n'
              f'Your next opportunity to become QA in GlobalLogic is '
              f'{self.SEARCH_PAGE.get_the_first_search_result().text}!')
