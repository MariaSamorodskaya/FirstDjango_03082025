from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.author),
    path('item/<int:id>', views.f_items),
    path('items', views.items_list),
]
