"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def account(name: str, surname: str, birth_year: int, city: str, email: str, tell: int):
    """
    """
    return '{0} {1} {2} {3} {4} {5}'.format(name,surname,birth_year,city,email,tell)


account(name = 'igor', surname = 'kuzmin', birth_year = 1996, city = 'moscow', email = 'igorkuz2018@yandex.ru', tell = 899977777)
