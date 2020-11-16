from actions import GoogleSearchActions
from actions import PyPiSearchActions
from actions import GLCareersSearchActions


def test_pypi_search_for_selenium(setup):
    KEYWORD = "selenium install ubuntu python"

    search_actions = GoogleSearchActions(setup)
    search_actions.search_by_keyword(KEYWORD)
    search_actions.open_search_result_by_address("pypi.org")

    KEYWORD = "selenium"

    search_actions = PyPiSearchActions(setup)
    search_actions.open_the_second_search_result(KEYWORD)


def test_gl_qa_job_search(setup):
    KEYWORD = "QA"

    search_actions = GLCareersSearchActions(setup)
    search_actions.print_first_found_job(KEYWORD)
