from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

items = [
        {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
        {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
        {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
        {"id": 7, "name": "Картофель фри" ,"quantity":0},
        {"id": 8, "name": "Кепка" ,"quantity":124},
    ]

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
            f"<a href = '/'>Домашняя /</a>"
            f"<a href = '/items'>Список товаров /</a>"
            f"<a href = '/about'>Об авторе</a><br><br>"
            f"<strong>Имя</strong>: <i>{dict1["name"]}</i><br>"
            f"<strong>Отчество</strong>: <i>{dict1["patronymic"]}</i><br>"
            f"<strong>Фамилия</strong>: <i>{dict1["surname"]}</i><br>"
            f"<strong>Телефон</strong>: <i>{dict1['phone']}</i><br>"
            f"<strong>e-mail</strong>: <i>{dict1['e-mail']}</i><br>"
    )                                               
    return HttpResponse(text1)


def f_items(request,id: int):
    for i in items:
        if i["id"] == id:
            context = i
            return render(request,'item_page.html', context)
    text = f"""
            <i>Товар с id= {id} не найден</i>
            <p><a href = '/items'> Назад к списку товаров</a></p>
            """     
    return HttpResponseNotFound(text)             

def items_list(request):
    context = {"items": items}
    return render(request, "items_list.html", context)


def main(request) -> HttpResponse:
    context = {
        "name": "Иванов Иван Петрович",
        "email": "my_mail@mail.ru"
    }
    return render(request,'index.html', context)
