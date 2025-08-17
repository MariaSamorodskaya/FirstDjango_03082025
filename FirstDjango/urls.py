from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main, name = "home"),
    path('item/<int:id_arg>', views.f_items, name = "item-detail"),
    path('items', views.items_list, name = "item-list"),
    path('about', views.author, name = "author"),



]
