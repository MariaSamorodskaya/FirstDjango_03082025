from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item, Color

# Create your views here.

"""
items = [
        {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
        {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
        {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
        {"id": 7, "name": "Картофель фри" ,"quantity":0},
        {"id": 8, "name": "Кепка" ,"quantity":124},
    ]
"""

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
     "email": "vasya@mail.ru"
     }
    context={"dict1":dict1}
    return render(request, "about.html", context)


def f_items(request,id_arg: int):
    try:
        items=Item.objects.get(id=id_arg)
        item_colors=items.colors.all()
        context = {"items": items, "item_colors": item_colors}
        return render(request,'item_page.html', context)
    
    except:
        context = {"id": id_arg}
        return render(request, "errors.html",context)

def items_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)


def main(request) -> HttpResponse:
    context = {
        "name": "Иванов Иван Петрович",
        "email": "my_mail@mail.ru"
    }
    return render(request,'index.html', context)

