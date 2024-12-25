import requests
import allure


class Kino_collection:
    """
    Класс содержит методы, выполняющие HTTP-запросы к API Кинопоиска.
    """

    def __init__(self, url):
        self.url = url

    @allure.step("Поиск информации")
    def get_movies(self, filtres=None, auth_token=None):
        """
        Метод реализует Универсальный поиск с фильтрами.
        """
        response = requests.get(
            self.url + "v1.4/movie", params=filtres, headers=auth_token
        )
        return response

    @allure.step("Поиск фильмов по названию")
    def get_movies_by_name(self, filtres: dict = {}, auth_token: str = ""):
        """
        Метод реализует Поиск фильмов по названию.
        """
        response = requests.get(
            self.url + "v1.4/movie/search", params=filtres, headers=auth_token
        )
        return response

    @allure.step("Поиск персон")
    def get_person_by_name(self, filtres: dict = {}, auth_token: str = ""):
        """
        Метод реализует Поиск персон по имени.
        """
        response = requests.get(
            self.url + "v1.4/person/search", params=filtres, headers=auth_token
        )
        return response
