from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <a href="/about">Иванов И.П.</a>
    """
    return HttpResponse(text)

def author(request):
    dict1 = {"name": "Иван",
     "patronymic": "Петрович",
     "surname": "Иванов",
     "phone": "8-923-600-01-02",
     "e-mail": "vasya@mail.ru"
     }
    text1 = (
            f"<strong>Имя</strong>: <i>{dict1["name"]}</i><br>"
            f"<strong>Отчество</strong>: <i>{dict1["patronymic"]}</i><br>"
            f"<strong>Фамилия</strong>: <i>{dict1["surname"]}</i><br>"
            f"<strong>Телефон</strong>: <i>{dict1['phone']}</i><br>"
            f"<strong>e-mail</strong>: <i>{dict1['e-mail']}</i><br>"
    )                                               
    return HttpResponse(text1)