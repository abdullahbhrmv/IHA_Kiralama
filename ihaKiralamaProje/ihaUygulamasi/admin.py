# ihaUygulamasi/admin.py

from django.contrib import admin
from .models import IHA, Kiralama

# IHA modelini admin paneline eklemek için
@admin.register(IHA)
class IHAAdmin(admin.ModelAdmin):
    list_display = ['marka', 'model', 'agirlik', 'kategori', 'fotograf']

# Kiralama modelini admin paneline eklemek için
@admin.register(Kiralama)
class KiralamaAdmin(admin.ModelAdmin):
    list_display = ['iha', 'tarih_baslangic', 'tarih_bitis', 'kiralayan_uye']
