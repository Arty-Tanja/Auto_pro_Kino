from pages.PostmanPage import Kino_collection
import allure

base_url = "https://api.kinopoisk.dev/"
x_api_key = "8K78K5K-ZKG4DVB-GTMKKPG-KB6R0VC"

api_key = {"X-API-KEY": f"{x_api_key}"}

kinopoisk = Kino_collection(base_url)


@allure.title("Автотест на поиск фильма по названию")
@allure.description("Позититвный тест-кейс на поиск по названию")
@allure.feature("Поиск фильма")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_name(filtres={"query": "Букшоп"},
     auth_token=api_key):
    """
    Поиск по названию
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на поиск по рейтингу")
@allure.description(
    "Позититвный тест-кейс на поиск\
                     по рейтингу выше 7"
)
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_rating(filtres={"rating.kp": "7.1-10"},
       auth_token=api_key):
    """
    Поиск по высокому рейтингу Кинопоиск
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на  поиск по жанру и году")
@allure.description(
    "Позититвный тест-кейс на поиск\
                     по жанру и году"
)
@allure.feature("Поиск фильмов")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_genre(
    filtres={"genres.name": "комедия", "year": "2023"},
    auth_token=api_key
):
    """
    Поиск по жанру и году
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


@allure.title("Автотест на поиск фильма")
@allure.description(
    "Негативный тест-кейс на поиск с\
                     некорректным названием"
)
@allure.feature("Поиск фильма")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_movies_by_incorrect_name(filtres={"query": "ookoo4%"},
       auth_token=api_key):
    """
    NEGATIVE Поиск несуществующего фильма
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] == 0


@allure.title("Автотест на поиск персоны")
@allure.description("Позитивный  тест-кейс на поиск по имени")
@allure.feature("Поиск персоны")
@allure.severity(allure.severity_level.NORMAL)
def test_get_persons_by_name(filtres={"query": "Стивен Спилберг"},
  auth_token=api_key):
    """
    Поиск персоны по имени
    """
    response = kinopoisk.get_person_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0
