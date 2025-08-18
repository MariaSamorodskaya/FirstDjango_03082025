from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name = "home"),
    path('item/<int:id_arg>', views.f_items, name = "item-detail"),
    path('items', views.items_list, name = "item-list"),
    path('about', views.author, name = "author"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




