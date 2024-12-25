from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Authorization:
    """
        Класс содержит методы для авторизации на сайте Кинопоиска.
    """

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()

    @allure.step("Поиск кнопки Войти и её нажатие.\
        Закрытие рекламного окна")
    def find_enter(self) -> None:
        """
            Метод закрывает рекламу и ищет  кнопку Войти.
        """
        try:  
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".styles_root__EjoL7").click()
        except NoSuchElementException:
            pass

        self._driver.find_element(By.CSS_SELECTOR,
                                  ".styles_loginButton__LWZQp").click()

    @allure.step("Авторизация с логином {username} и паролем {password}")
    def authorization(self, timeout: int, username: str, password: str)\
        -> None:
        """
            Метод реализует заполнение полей Логин или email,
        нажатие кнопки Войти, ввод пароля и нажатие кнопки Продолжить.
        """
        self._driver.implicitly_wait(timeout)
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        try:
            self._driver.find_element(By.CSS_SELECTOR,
                                      ".PasswordButton").click()
        except NoSuchElementException:
            pass
        WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="passp-field-passwd"]')
            )
        )
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').\
            send_keys(password)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        
    @allure.step("Заполнение поля Пароль невалидным значением\
                 {password}")    
    def incorrect_password(self, timeout: int, username: str, password: str)\
        -> str:
        """
          Метод заполняет поле логин валидными данными
          и поле пароль невалидными данными и выводт
          сообщение об ошибке.
        """
        self._driver.implicitly_wait(timeout)
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="passp-field-passwd"]')
            )
        )
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').\
            send_keys(password)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        message = WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="field:input-passwd:hint"]')
            )
        ).text
        return message
 
    @allure.step("Заполнение поля Логин или email невалидным значением\
                 {username}")
    def incorrect_login(self, timeout: int, username: str) -> str:
        """
            Метод заполняет поле логин невалиднывми данными и  возвращает текст сообщения об ошибке.
        """
        self._driver.implicitly_wait(timeout)
        self._driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').\
            send_keys(username)
        self._driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').\
            click()
        WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="field:input-login:hint"]')
            )
        )
        message = self._driver.\
            find_element(By.XPATH, '//*[@id="field:input-login:hint"]').text
        return message
