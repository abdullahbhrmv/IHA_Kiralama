# ihaUygulamasi/urls.py

from django.urls import path
from .views import home, iha_list, iha_detail, iha_create, iha_update, iha_delete, kiralama_list, kiralama_detail, kiralama_create, kiralama_delete, kiralama_update, login, register, register_user, logout, mevcut_iha_listesi

urlpatterns = [
    path('', home, name='home'),
    path('', mevcut_iha_listesi, name='mevcut_iha_listesi'),
    path('iha-list/', iha_list, name='iha_list'),
    path('iha-detail/<int:iha_id>/', iha_detail, name='iha_detail'),
    path('iha-create/', iha_create, name='iha_create'),
    path('iha-update/<int:iha_id>/', iha_update, name='iha_update'),
    path('iha-delete/<int:iha_id>/', iha_delete, name='iha_delete'),

    path('kiralama_list/', kiralama_list, name='kiralama_list'),
    path('kiralama_detail/<int:kiralama_id>/', kiralama_detail, name='kiralama_detail'),
    path('kiralama_create/', kiralama_create, name='kiralama_create'),
    path('kiralama_update/<int:kiralama_id>/', kiralama_update, name='kiralama_update'),
    path('kiralama_delete/<int:kiralama_id>/', kiralama_delete, name='kiralama_delete'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register_user/', register_user, name='register_user'),
    path('logout/', logout, name='logout'),
]
