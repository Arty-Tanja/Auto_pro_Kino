import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from pages.AuthPage import Authorization
from pages.MainPage import Search
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def resolving_captcha(driver, timeout=60):
    """
        Функция ставит галочку "Я не робот", затем капча решается руками.
        Далее функция закрывает рекламное окно.
    """
    try:  
        driver.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
    except NoSuchElementException:
        pass

    try:  
        WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, ".styles_root__EjoL7")
            )
        )
        driver.find_element(By.CSS_SELECTOR, ".styles_root__EjoL7").click()
    except TimeoutException:
        pass
    except NoSuchElementException:
        pass


@pytest.mark.parametrize("login, alert",
                         [("mikurova.t@yandex.ru", "Логин введен некорректно или удален")
                          ])
def test_neg_incorrect_login(login, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha(browser)
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_login(3, login) == alert

    browser.quit()


@pytest.mark.parametrize("login, password, alert",
                         [("mikurova.tanja@yandex.ru", "123 ", "Неверный пароль")
                          ])
def test_neg_incorrect_password(login, password, alert):
    browser = webdriver.Chrome()

    authorization_page = Authorization(browser)
    resolving_captcha(browser)
    authorization_page.find_enter()
    assert authorization_page.\
        incorrect_password(3, login, password) == alert

    browser.quit()


@pytest.mark.parametrize("query", ["До встречи на Венере"])
def test_find_movie(query):
    browser = webdriver.Chrome()
   

    search_page = Search(browser)
    resolving_captcha(browser)

    assert search_page.search_query(query) != 0

    browser.quit()


@pytest.mark.parametrize("query", ["Стивен Спилберг"])
def test_find_person(query):
    browser = webdriver.Chrome()
   

    search_page = Search(browser)
    resolving_captcha(browser)

    assert search_page.search_query(query) != 0

    browser.quit()


@pytest.mark.parametrize("query", ["ookoo4%"])
def test_negative_find_movie(query):
    browser = webdriver.Chrome()

    search_page = Search(browser)
    resolving_captcha(browser)

    assert search_page.search_query(query) == 0

    browser.quit()






