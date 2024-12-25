from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import allure


class Search:
    """
    Класс содержит методы для поиска фильмов, сериалов, персон.
    """

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()

    @allure.step("Поиск через поисковую строку")
    def search_query(self, query: str) -> int:
        """
        Метод закрывает рекламу и реализует\
        поиск через поисковую строку.
        """
        try:
            self._driver.find_element(
                By.CSS_SELECTOR, ".styles_root__EjoL7").click()
        except NoSuchElementException:
            pass

        self._driver.find_element(By.TAG_NAME, "input").send_keys(query)
        self._driver.find_element(
            By.CSS_SELECTOR, ".search-form-submit-button__icon"
        ).click()
        result_text = self._driver.find_element(
            By.CSS_SELECTOR, ".search_results_topText"
        ).text
        result_list = result_text.split(": ")

        return int(result_list[2])
