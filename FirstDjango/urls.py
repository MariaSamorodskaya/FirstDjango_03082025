from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('about', views.author),
    path('item/<int:id_arg>', views.f_items),
    path('items', views.items_list),
    path('about', views.author),



]
