from Auto_pro_Kino.pages.PostmanPage import ProjectAPI

base_url = "https://api.kinopoisk.dev/"
x_api_key = "8K78K5K-ZKG4DVB-GTMKKPG-KB6R0VC"

api_key = {
    "X-API-KEY": f"{x_api_key}"
}

kinopoisk = ProjectAPI(base_url)


def test_get_movies_by_name(filtres={"query": "Букшоп"},
                            auth_token=api_key):
    """
         Поиск по названию
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


def test_get_movies_by_rating(filtres={"rating.kp": "7.1-10"},
                              auth_token=api_key):
    """
         Поиск по высокому рейтингу Кинопоиск
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


def test_get_movies_by_genre(filtres={"genres.name": "комедия",
                                      "year": "2023"},
                             auth_token=api_key):
    """
        Поиск по жанру и году
    """
    response = kinopoisk.get_movies(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0


def test_get_movies_by_incorrect_name(filtres={"query": "ookoo4%"},
                                      auth_token=api_key):
    """
        NEGATIVE Поиск несуществующего фильма
    """
    response = kinopoisk.get_movies_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] == 0

def test_get_persons_by_name(filtres={"query": "Стивен Спилберг"},
                            auth_token=api_key):
    """
         Поиск персоны по имени
    """
    response = kinopoisk.get_person_by_name(filtres, auth_token)
    assert response.status_code == 200
    movie_list = response.json()
    assert movie_list["total"] != 0